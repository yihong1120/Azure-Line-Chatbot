from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError
import datetime
import logging
from config import AppConfig
from typing import Any

config = AppConfig()

class AzureBlobLogger:
    def __init__(self) -> None:
        """
        Initialises the AzureBlobLogger which sets up a connection to Azure Blob Storage.
        It also configures the container for logging.
        """
        connection_string: str = config.get_value("AZURE_BLOB_STORAGE_CONNECTION_STRING")
        self.blob_service_client: BlobServiceClient = BlobServiceClient.from_connection_string(connection_string)
        current_date: str = datetime.datetime.now().strftime('%Y%m%d')
        self.log_blob_name: str = f"{current_date}.log"
        self.container_name: str = config.get_value("CONTAINER_NAME")
        self.setup_container()

    def setup_container(self) -> None:
        """
        Sets up the container in Azure Blob Storage. 
        Creates the container if it doesn't exist.
        """
        container_client = self.blob_service_client.get_container_client(self.container_name)
        if not container_client.exists():
            self.blob_service_client.create_container(self.container_name)

    def get_handler(self) -> "AzureBlobHandler":
        """
        Returns a logging handler for Azure Blob storage.

        Returns:
            AzureBlobHandler: The custom logging handler for Azure Blob.
        """
        return AzureBlobHandler(self.blob_service_client, self.container_name, self.log_blob_name)


class AzureBlobHandler(logging.Handler):
    def __init__(self, blob_service_client: BlobServiceClient, container_name: str, blob_name: str) -> None:
        """
        Initialises the AzureBlobHandler which provides a logging handler that writes 
        log messages to Azure Blob storage.

        Args:
            blob_service_client (BlobServiceClient): The client to interact with Azure Blob Storage.
            container_name (str): Name of the container in Azure Blob Storage.
            blob_name (str): Name of the blob (log file) in the container.
        """
        super().__init__()
        self.blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        self._is_emitting: bool = False  # Guard against recursion
        try:
            self.blob_client.create_append_blob()
        except ResourceExistsError as e:
            print(f'Blob already exists: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')

    def emit(self, record: logging.LogRecord) -> None:
        """
        Emits a log record to Azure Blob Storage.

        Args:
            record (logging.LogRecord): The log record to be emitted.
        """
        if self._is_emitting:
            return
        self._is_emitting = True
        try:
            log_entry: str = self.format(record) + '\n'
            self.blob_client.append_block(log_entry)
        except Exception as e:
            # Instead of logging the error, we'll just print it to avoid recursion
            print(f"Error while appending to blob: {e}")
        finally:
            self._is_emitting = False
