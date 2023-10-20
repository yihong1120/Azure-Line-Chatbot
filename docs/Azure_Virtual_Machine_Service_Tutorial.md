# Azure Virtual Machine Service Setup and Usage Tutorial

This tutorial will guide you through the process of applying for and using Azure Virtual Machine Service. 

## Step 1: Create a Windows Virtual Machine in the Azure Portal

To create a Windows virtual machine in the Azure portal, follow these steps:

1. Sign in to the Azure portal.
2. Enter "virtual machines" in the search bar and select "Virtual machines" under Services.
3. Click on "Create" and then select "Azure virtual machine".
4. On the "Create a virtual machine" page, provide the necessary details such as the virtual machine name, image, administrator account, and inbound port rules.
5. Review the settings and click on "Review + create".
6. After validation, click on "Create" to deploy the virtual machine.
7. Once the deployment is complete, you can access the virtual machine by selecting "Go to resource".

For detailed step-by-step instructions, you can refer to the [Quickstart: Create a Windows virtual machine in the Azure portal](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/quick-create-portal) tutorial.

## Step 2: Connect to the Virtual Machine and Install Web Server

To connect to the virtual machine and install a web server, follow these steps:

1. Create a remote desktop connection to the virtual machine. You can use the Remote Desktop Client for Windows or a compatible RDP client for Mac.
2. On the overview page of your virtual machine, select "Connect" and then "RDP".
3. In the "Connect with RDP" tab, choose the default options and click on "Download RDP file".
4. Open the downloaded RDP file and click "Connect" when prompted.
5. In the Windows Security window, select "More choices" and then "Use a different account".
6. Enter the username as `localhost\username` and the password you created for the virtual machine.
7. Click "OK" to establish the connection.
8. Once connected, open a PowerShell prompt on the virtual machine and run the following command to install the IIS web server:

   ```
   Install-WindowsFeature -name Web-Server -IncludeManagementTools
   ```

9. After the installation is complete, you can close the RDP connection to the virtual machine.

For more information on monitoring changes and updating a Windows virtual machine in Azure, you can refer to the [Learn Azure Virtual Machines Windows Tutorial: Monitor changes and update a Windows virtual machine in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/tutorial-config-management) tutorial.

## Step 3: Clean Up Resources

When you no longer need the virtual machine and its associated resources, you can delete them to avoid unnecessary costs. Follow these steps to delete the resources:

1. On the overview page of the virtual machine, select the "Resource group" link.
2. At the top of the resource group page, select "Delete resource group".
3. Follow the prompts to confirm the deletion of the resources and the resource group.

## Additional Resources

- [Introduction to Azure Virtual Machines](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-virtual-machines/)
- [Azure Virtual Machines Documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/)

Please note that the actual steps and options may vary depending on your specific requirements and the Azure portal interface.

Remember to refer to the official Azure documentation for the most up-to-date and detailed instructions.

