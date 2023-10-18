import pyodbc
import logging
from config import AppConfig
from typing import List, Dict, Union

config = AppConfig()

class AzureDatabase:
    def __init__(self) -> None:
        """
        Initialise the AzureDatabase class.
        
        This class handles the interactions with the database stored in Azure.
        It sets up the connection, creates tables if they don't exist, and 
        provides methods to fetch and insert data.
        """
        # Configure database settings from the AppConfig
        self.DATABASE_CONFIG = {
            'Driver': config.get_value("Driver").strip(),
            'Server': config.get_value("DB_Server").strip(),
            'Database': config.get_value("Database").strip(),
            'UID': config.get_value("DB_UID").strip(),
            'PWD': config.get_value("DB_PWD").strip(),
            'charset': config.get_value("charset").strip()
        }
        
        # Create a connection string and establish a connection
        self.connection_string = ";".join([f"{k}={v}" for k, v in self.DATABASE_CONFIG.items()])
        self.connection = pyodbc.connect(self.connection_string)
        
        # Ensure necessary tables exist
        self.create_table()

    def create_table(self) -> None:
        """
        Create the ChatHistory table if it doesn't exist.
        """
        cursor = self.connection.cursor()
        cursor.execute('''
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ChatHistory' AND xtype='U')
            CREATE TABLE ChatHistory (
                id INT PRIMARY KEY IDENTITY(1,1),
                user_id VARCHAR(255),
                role VARCHAR(50),
                content TEXT
            )
        ''')
        self.connection.commit()

    def get_user_history(self, user_id: str, max_history: int) -> List[Dict[str, str]]:
        """
        Fetch the chat history for a specific user.

        Args:
            user_id (str): The unique identifier for the user.
            max_history (int): Maximum number of chat messages to fetch.

        Returns:
            List[Dict[str, str]]: List of dictionaries with role and content of the chat.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT TOP (?) role, content FROM ChatHistory WHERE user_id = ? ORDER BY id DESC", (max_history, user_id))
        rows = cursor.fetchall()
        return [{"role": row.role, "content": row.content} for row in rows]

    def append_to_user_history(self, user_id: str, role: str, message: str) -> None:
        """
        Insert a new message into the user's chat history.

        Args:
            user_id (str): The unique identifier for the user.
            role (str): The role, either "user" or "assistant".
            message (str): The content of the message.

        Note:
            If there's an error while inserting, the operation will be rolled back.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO ChatHistory (user_id, role, content) VALUES (?, ?, ?)", (user_id, role, message))
            self.connection.commit()
        except Exception as e:
            logging.error(f"Error whilst inserting data into the database: {e}")
            self.connection.rollback()