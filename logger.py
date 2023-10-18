from azure.storage.blob import BlobServiceClient
import datetime
import logging
from config import AppConfig

config = AppConfig()

class AzureBlobLogger:
    def __init__(self):
        connection_string = config.get_value("AZURE_BLOB_STORAGE_CONNECTION_STRING")
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        current_date = datetime.datetime.now().strftime('%Y%m%d')
        self.log_blob_name = f"{current_date}.log"
        self.container_name = config.get_value("CONTAINER_NAME")
        self.setup_container()

    def setup_container(self):
        container_client = self.blob_service_client.get_container_client(self.container_name)
        if not container_client.exists():
            self.blob_service_client.create_container(self.container_name)

    def get_handler(self):
        return AzureBlobHandler(self.blob_service_client, self.container_name, self.log_blob_name)


class AzureBlobHandler(logging.Handler):
    def __init__(self, blob_service_client, container_name, blob_name):
        super().__init__()
        self.blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        self._is_emitting = False  # Guard against recursion
        try:
            self.blob_client.create_append_blob()
        except:
            pass

    def emit(self, record):
        if self._is_emitting:
            return
        self._is_emitting = True
        try:
            log_entry = self.format(record) + '\n'
            self.blob_client.append_block(log_entry)
        except Exception as e:
            # Instead of logging the error, we'll just print it to avoid recursion
            print(f"Error while appending to blob: {e}")
        finally:
            self._is_emitting = False