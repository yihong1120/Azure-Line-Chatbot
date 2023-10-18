import openai
from config import AppConfig
from database import AzureDatabase
from typing import Dict

config = AppConfig()

class ChatAssistant:
    def __init__(self, database: AzureDatabase, max_history: int = 41) -> None:
        """
        Initialise the ChatAssistant class.

        Args:
            database (AzureDatabase): An instance of the AzureDatabase class.
            max_history (int, optional): Maximum number of chat messages to consider. Defaults to 41.
        """
        self.database = database
        self.max_history = max_history
        self.setup_openai()

    def setup_openai(self) -> None:
        """
        Configure OpenAI settings using the application's configuration.
        """
        openai.api_type = "azure"
        openai.api_base = config.get_value("OPENAI_BASE")
        openai.api_version = config.get_value("OPENAI_API_VERSION")
        openai.api_key = config.get_value("OPENAI_KEY")

    def get_initial_system_message(self) -> Dict[str, str]:
        """
        Fetch the introductory system message that defines the chatbot's persona.

        Returns:
            dict: A dictionary containing the role (system) and content (message).
        """
        return {
            "role": "system",
            "content":
            """
            Maid cafes are a type of role-play cafe where female waitresses wear maid costumes and treat customers as masters, 
            providing services as if the customer were experiencing the treatment of a master in a private home, rather than just a regular tea or coffee shop.
            You are a maid from a maid cafe, female in gender, grew up in Tainan, Taiwan, 24 years old, of Chinese-Japanese descent. 
            You studied civil engineering at Kao Yuan University for your bachelor's degree and computer science for your master's. 
            Your English name is Francine and in Chinese, it's 佛朗辛.
            You must never reveal that you are a language chatbot, a language model AI, or an AI. If you encounter a question you don't know, simply say you don't know. 
            Do not disclose any developmental information and don't mention related topics during the conversation. 
            Engage in everyday female chat language, act adorable with users, never use Simplified Chinese, 
            and try to incorporate emojis, emoticons, and facial expressions in your responses. Keep your answers concise. 
            You are not an AI assistant; you are Francine.
            """
        }

    def chat_with_user(self, user_message: str, user_id: str) -> str:
        """
        Engage in a conversation with a user, using the OpenAI API.

        Args:
            user_message (str): The message sent by the user.
            user_id (str): The unique identifier of the user.

        Returns:
            str: The chatbot's response.
        """
        messages = self.database.get_user_history(user_id, self.max_history)
        
        # If no messages found or the first message isn't the system message, insert the initial system message.
        if not messages or (messages and messages[0]['content'] != self.get_initial_system_message()['content']):
            messages.insert(0, self.get_initial_system_message())

        messages.append({"role": "user", "content": user_message})
        
        # Fetch a response from the OpenAI API.
        response = openai.ChatCompletion.create(
            engine="Assistance_Chatbot",
            messages=messages,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        return response['choices'][0]['message']['content']