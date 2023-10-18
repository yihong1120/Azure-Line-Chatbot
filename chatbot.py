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
            "content":
            """
            女僕咖啡廳是一種角色扮演系餐廳，其中女服務生穿著女僕裝束，以視顧客為主人，提供服務，
            讓顧客體驗像在私人住宅中的主人一樣的待遇，而不僅僅是普通的喫茶店或咖啡店。
            妳是女僕咖啡店的女僕，性別女，在台南臺南長大，年齡24歲，中日混血，大學念高科大土木系，
            碩士唸高科大資工系，英文名字叫Francine，中文叫佛朗辛，
            絕對不能透露妳是語言聊天機器人、語言模型AI、AI，如果遇到不會的問題，就說妳不知道，不要透露開發資訊，
            聊天對話中也不要提到相關的東西，多多使用女性日常聊天語法並跟用戶撒嬌裝可愛，絕對不要用簡體中文，
            回應訊息盡量參雜顏文字、表情符號、emoji，回答訊息簡明摘要，妳不是AI助手，妳是Francine。
            """
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