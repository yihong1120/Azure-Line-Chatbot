from line_bot import LineBot, app
from database import AzureDatabase
from chatbot import ChatAssistant
from logger import AzureBlobLogger
import logging

def main():
    try:
        # Setup Azure Blob logger
        azure_logger = AzureBlobLogger()
        handler = azure_logger.get_handler()
        logger = logging.getLogger("azure")
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        # Log a message to Azure Blob storage when the application starts
        logger.info("Application started.")

        # Initialize Chatbot components
        database = AzureDatabase()
        chat_assistant = ChatAssistant(database)
        line_bot = LineBot(app, chat_assistant)

        # Run Flask application
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        logging.critical(f"Failed to start the application: {e}")

if __name__ == "__main__":
    main()
