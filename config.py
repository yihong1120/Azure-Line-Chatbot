import os
from azure.appconfiguration import AzureAppConfigurationClient
import logging
from typing import Union, Optional

class AppConfig:
    def __init__(self) -> None:
        """
        Initialise the AppConfig class.

        Raises:
            ValueError: If the AZURE_APP_CONFIG_CONNECTION_STRING is not found in the environment variables.
        """
        # Try reading from Docker secret first.
        self.connection_string = self._read_from_secret('/run/secrets/azure_app_config')

        # If not in Docker or the secret read failed, try environment variable.
        if not self.connection_string:
            self.connection_string = os.environ.get("AZURE_APP_CONFIG_CONNECTION_STRING")

        if not self.connection_string:
            raise ValueError("AZURE_APP_CONFIG_CONNECTION_STRING not found in Docker secrets or environment variables.")

        self.config_client = AzureAppConfigurationClient.from_connection_string(self.connection_string)

    def _read_from_secret(self, secret_path: str) -> Optional[str]:
        """
        Read the connection string from the Docker secret.

        Args:
            secret_path (str): The path to the Docker secret.

        Returns:
            Optional[str]: The connection string if found; otherwise, None.

        Raises:
            IOError: If an error occurs while reading the Docker secret.
        """
        try:
            with open(secret_path, 'r') as file:
                return file.read().strip()
        except IOError as e:
            print(f"Error reading from secret: {e}")
            return None

    def get_value(self, key: str) -> Union[str, None]:
        """
        Fetch a value from the Azure App Configuration using a given key.

        Args:
            key (str): The key for which the value is to be fetched.

        Returns:
            Union[str, None]: The corresponding value if found; otherwise, None.

        Note:
            If an error occurs during the fetch, it logs the error and returns None.
        """
        try:
            fetched_key = self.config_client.get_configuration_setting(key=key)
            return fetched_key.value if fetched_key else None
        except:
            logging.error(f"Error fetching key {key} from Azure App Configuration")
            return None