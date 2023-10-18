# Azure-Line-Chatbot

An integrated chatbot solution combining the prowess of OpenAI's GPT models, the robust infrastructure of Azure, and the widespread usability of the LINE messaging platform.

## Description

Azure-Line-Chatbot is crafted to bring a seamless user experience, providing meaningful interactions through the LINE messaging platform. This repository encapsulates the end-to-end workflow, from fetching configurations from Azure App Configuration, storing conversational logs in Azure Blob Storage, to real-time chatbot interactions powered by OpenAI.

## Features

- **Azure Integration**: Utilise Azure services for configuration management and data storage.
- **OpenAI GPT**: Leverage state-of-the-art chatbot functionalities for engaging user interactions.
- **LINE Messaging API**: Directly connect with users on the popular LINE platform.

## Installation & Setup

1. **Clone the Repository**:
   ```
   git clone https://github.com/yihong1120/Azure-Line-Chatbot.git
   cd Azure-Line-Chatbot
   ```

2. **Set Up Virtual Environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Environment Variables**: Ensure you've set up necessary environment variables or configuration files for Azure connection strings and LINE API keys.

5. **Run the Application**:
   ```
   python app.py
   ```

## Usage

After setting up, simply interact with the bot using the LINE application. Your messages will be processed by the OpenAI model, and you'll receive a response in real-time.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yihong1120/Azure-Line-Chatbot.git/issues).

## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/yihong1120/Azure-Line-Chatbot/blob/main/LICENSE) for more information.