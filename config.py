import os
from azure.appconfiguration import AzureAppConfigurationClient
import logging

class AppConfig:
    def __init__(self) -> None:
        """
        Initialise the AppConfig class.

        Raises:
            ValueError: If the AZURE_APP_CONFIG_CONNECTION_STRING is not found in the environment variables.
        """
        self.connection_string = os.environ.get("AZURE_APP_CONFIG_CONNECTION_STRING")
        
        # Ensure the connection string exists
        if not self.connection_string:
            raise ValueError("AZURE_APP_CONFIG_CONNECTION_STRING not found in environment variables.")
        
        # Initialise the Azure App Configuration client
        self.config_client = AzureAppConfigurationClient.from_connection_string(self.connection_string)

    def get_value(self, key: str) -> Union[str, None]:
        """
        Fetch a value from the Azure App Configuration using a given key.

        Args:
            key (str): The key for which the value is to be fetched.

        Returns:
            Union[str, None]: The corresponding value if found, otherwise None.

        Note:
            If an error occurs during the fetch, it logs the error and returns None.
        """
        try:
            fetched_key = self.config_client.get_configuration_setting(key=key)
            return fetched_key.value if fetched_key else None
        except:
            logging.error(f"Error fetching key {key} from Azure App Configuration")
            return None
