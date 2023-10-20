# Azure App Configuration Setup and Usage Tutorial with Python

This tutorial will guide you through the process of setting up and using Azure App Configuration with Python.

## Prerequisites

Before you start, make sure you have installed:

- Python 3.6 or later
- Azure App Configuration client library for Python

## Step 1: Sign in to the Azure portal

Sign in to the Azure portal at https://portal.azure.com/.

## Step 2: Create a new App Configuration

1. On the Azure portal menu or from the Home page, select **Create a resource**.
2. On the **Create a resource** page, search for **App Configuration** and select it.
3. In the **App Configuration** pane, select **Create**.

## Step 3: Fill out the Basics tab

Fill out the mandatory information required on the Basics tab. This is a minimum set of information required to provision an App Configuration.

## Step 4: Install the Azure App Configuration client library

Install the Azure App Configuration client library by using the pip install command:

```python
pip install azure-appconfiguration
```

## Step 5: Create a Python Script

Create a new file called `app-configuration-example.py` in the `app-configuration-example` directory and add the following code:

```python
from azure.appconfiguration import AzureAppConfigurationClient

connection_string = "<your_connection_string>"

client = AzureAppConfigurationClient.from_connection_string(connection_string)

# Add a new key-value
added_kv = client.add_configuration_setting("my_key", "my_value")

# Retrieve a stored key-value
retrieved_kv = client.get_configuration_setting(key="my_key")

print(retrieved_kv.value)  # Output: my_value
```

Replace `<your_connection_string>` with the connection string of your App Configuration.

## Step 6: Run the Python Script

Run your script:

```python
python app-configuration-example.py
```

## Step 7: Clean up resources

When you're done with the App Configuration, you can delete it to avoid incurring any further costs.

For more detailed instructions, you can refer to the official Azure App Configuration quickstart guide [here](https://learn.microsoft.com/en-us/azure/azure-app-configuration/quickstart-python).

Please note that the actual steps may vary slightly depending on the current Azure portal interface and the specific requirements of your project.

## References

- [Quickstart: Create an App Configuration store by using the Azure portal](https://learn.microsoft.com/en-us/azure/azure-app-configuration/quickstart-portal)
- [Quickstart: Use Azure App Configuration in a Python application](https://learn.microsoft.com/en-us/azure/azure-app-configuration/quickstart-python)
- [Azure App Configuration client library for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/appconfiguration-readme?view=azure-python)
