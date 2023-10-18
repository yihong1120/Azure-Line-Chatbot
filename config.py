import os
from azure.appconfiguration import AzureAppConfigurationClient
import logging

class AppConfig:
    def __init__(self):
        self.connection_string = os.environ.get("AZURE_APP_CONFIG_CONNECTION_STRING")
        if not self.connection_string:
            raise ValueError("AZURE_APP_CONFIG_CONNECTION_STRING not found in environment variables.")
        self.config_client = AzureAppConfigurationClient.from_connection_string(self.connection_string)

    def get_value(self, key):
        try:
            fetched_key = self.config_client.get_configuration_setting(key=key)
            return fetched_key.value if fetched_key else None
        except:
            logging.error(f"Error fetching key {key} from Azure App Configuration")
            return None
