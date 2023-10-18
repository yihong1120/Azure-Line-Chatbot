import openai
from config import AppConfig
from database import AzureDatabase

config = AppConfig()

class ChatAssistant:
    def __init__(self, database, max_history=41):
        self.database = database
        self.max_history = max_history
        self.setup_openai()

    def setup_openai(self):
        openai.api_type = "azure"
        openai.api_base = config.get_value("OPENAI_BASE")
        openai.api_version = config.get_value("OPENAI_API_VERSION")
        openai.api_key = config.get_value("OPENAI_KEY")

    def get_initial_system_message(self):
        return {
            "role": "system",
            "content": """..."""  # The original system message goes here.
        }

    def chat_with_user(self, user_message, user_id):
        messages = self.database.get_user_history(user_id, self.max_history)
        if not messages or (messages and messages[0]['content'] != self.get_initial_system_message()['content']):
            messages.insert(0, self.get_initial_system_message())
        messages.append({"role": "user", "content": user_message})
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