# Azure Blob Storage Setup and Usage Tutorial

This tutorial will guide you through the process of setting up and using Azure Blob Storage.

## Prerequisites

Before you start, make sure you have installed:

- Azure Storage Explorer (latest version)

## Step 1: Sign in to the Azure portal

Sign in to the Azure portal at https://portal.azure.com/.

## Step 2: Create a new Storage Account

1. On the Azure portal menu or from the Home page, select **Create a resource**.
2. On the **Create a resource** page, search for **Storage Account** and select it.
3. In the **Storage Account** pane, select **Create**.

## Step 3: Fill out the Basics tab

Fill out the mandatory information required on the Basics tab. This is a minimum set of information required to provision a Storage Account.

## Step 4: Create a Blob Container

1. To create a container, expand the storage account you created in the preceding step. 
2. Select Blob Containers, right-click and select Create Blob Container. 
3. Enter the name for your blob container. 

## Step 5: Upload Blobs to the Container

1. On the container ribbon, select Upload. This operation gives you the option to upload a folder or a file.
2. Choose the files or folder to upload. Select the blob type. Acceptable choices are Append, Page, or Block blob.

## Step 6: View Blobs in a Container

In the Azure Storage Explorer application, select a container under a storage account. The main pane shows a list of the blobs in the selected container.

## Step 7: Download Blobs

To download blobs using Azure Storage Explorer, with a blob selected, select Download from the ribbon. A file dialog opens and provides you the ability to enter a file name. Select Save to start the download of a blob to the local location.

## Step 8: Clean up resources

When you're done with the storage account, you can delete it to avoid incurring any further costs.

For more detailed instructions, you can refer to the official Azure Blob Storage quickstart guide [here](https://learn.microsoft.com/en-us/azure/storage/blobs/quickstart-storage-explorer).

Please note that the actual steps may vary slightly depending on the current Azure portal interface and the specific requirements of your project.

## References

- [Introduction to Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)
- [Quickstart: Use Azure Storage Explorer to create a blob](https://learn.microsoft.com/en-us/azure/storage/blobs/quickstart-storage-explorer)
- [Get started with Azure Blob Storage using .NET](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-dotnet-get-started)
- [Azure Blob Storage Tutorial](https://www.golinuxcloud.com/azure-blob-storage-tutorial/)
