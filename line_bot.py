from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import logging
from chatbot import ChatAssistant
from config import AppConfig

app = Flask(__name__)
config = AppConfig()

class LineBot:
    def __init__(self, app: Flask, chat_assistant: ChatAssistant) -> None:
        """
        Initialise the LineBot class.
        
        This class manages the interactions between the LINE messaging API 
        and the chat assistant bot.
        
        Args:
            app (Flask): The Flask application instance.
            chat_assistant (ChatAssistant): The instance of ChatAssistant class.
        """
        self.app = app
        self.line_bot_api = LineBotApi(config.get_value("LINE_CHANNEL_ACCESS_TOKEN"))
        self.handler = WebhookHandler(config.get_value("LINE_CHANNEL_SECRET"))
        self.chat_assistant = chat_assistant
        self.init_routes()

    def init_routes(self) -> None:
        """
        Initialise the routes for the webhook callbacks.
        
        This sets up the necessary endpoints to receive incoming messages from 
        the LINE messaging platform and send responses back.
        """
        @app.route("/webhook", methods=['POST'])
        def callback():
            signature = request.headers['X-Line-Signature']
            body = request.get_data(as_text=True)

            # Ensure the request is valid
            if not signature or not body:
                logging.warning("Received invalid request")
                abort(400)

            try:
                self.handler.handle(body, signature)
            except InvalidSignatureError:
                logging.error("Invalid signature error")
                abort(400)
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                abort(500)

            return 'OK'

        @self.handler.add(MessageEvent, message=TextMessage)
        def handle_text_message(event: MessageEvent) -> None:
            """
            Handle incoming text messages from users.
            
            This method retrieves the message from the user, processes it using 
            the chat assistant, and sends back the assistant's response.

            Args:
                event (MessageEvent): The event object containing message details.
            """
            user_message = event.message.text

            # Ensure the message is not empty
            if not user_message.strip():
                logging.warning("Received empty user message")
                return

            try:
                self.chat_assistant.database.append_to_user_history(event.source.user_id, "user", user_message)
                assistant_response = self.chat_assistant.chat_with_user(user_message, event.source.user_id)
                self.chat_assistant.database.append_to_user_history(event.source.user_id, "assistant", assistant_response)
                self.line_bot_api.reply_message(event.reply_token, TextSendMessage(text=assistant_response))
            except LineBotApiError as e:
                logging.error(f"Error responding to message: {e}")
            except Exception as e:
                logging.error(f"Unexpected error: {e}")