import pyodbc
import logging
from config import AppConfig

config = AppConfig()

class AzureDatabase:
    def __init__(self):
        self.DATABASE_CONFIG = {
            'Driver': config.get_value("Driver").strip(),
            'Server': config.get_value("DB_Server").strip(),
            'Database': config.get_value("Database").strip(),
            'UID': config.get_value("DB_UID").strip(),
            'PWD': config.get_value("DB_PWD").strip(),
            'charset': config.get_value("charset").strip()
        }
        self.connection_string = ";".join([f"{k}={v}" for k, v in self.DATABASE_CONFIG.items()])
        self.connection = pyodbc.connect(self.connection_string)
        self.create_table()

    def create_table(self):
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

    def get_user_history(self, user_id, max_history):
        cursor = self.connection.cursor()
        cursor.execute("SELECT TOP (?) role, content FROM ChatHistory WHERE user_id = ? ORDER BY id DESC", (max_history, user_id))
        rows = cursor.fetchall()
        return [{"role": row.role, "content": row.content} for row in rows]

    def append_to_user_history(self, user_id, role, message):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO ChatHistory (user_id, role, content) VALUES (?, ?, ?)", (user_id, role, message))
            self.connection.commit()
        except Exception as e:
            logging.error(f"Error while inserting data into the database: {e}")
            self.connection.rollback()