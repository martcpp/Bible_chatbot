# WhatsApp Scripture Chatbot

## Overview

The **WhatsApp Scripture Chatbot** is a Python-based chatbot designed to facilitate the reading and explanation of scriptures from the bible. It utilizes the WhatsApp Business API to allow users to interact with the bot through WhatsApp. Users can send scripture references or questions, and the chatbot responds with explanations or references from the scriptures.

## Features

- Interpretation of scriptures from the bible.
- Explanation of selected scriptures.
- Support for user queries and questions.
- Seamless integration with WhatsApp for user interaction.
- Extensibility to incorporate additional scriptures and features.

## Prerequisites

Before deploying and running the WhatsApp Scripture Chatbot, ensure you have the following prerequisites in place:

1. **WhatsApp Business Account:** Create or convert a WhatsApp Business Account for your bot.

2. **Phone Number with SIM Card:** You'll need a phone number with a functional SIM card capable of receiving SMS or voice calls for verification during the WhatsApp Business API setup.

3. **Server or Hosting:** Set up a server or utilize cloud hosting services such as AWS, Google Cloud, Azure, or others to host your bot's code and the WhatsApp Business API.

4. **WhatsApp Business API Access:** Apply for access to the WhatsApp Business API through WhatsApp's official Business API providers.

5. **Programming Language and Dependencies:** The bot is constructed using Python and relies on the Flask framework to handle incoming WhatsApp messages and provide scripture explanations.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/martcpp/Bible_chatbot.git
   ```

2. **Install dependencies:**
   ```bash
   cd Bible_chatbot
   pip install -r requirements.txt
   ```

3. **Configure WhatsApp Business API:** Follow the instructions provided by WhatsApp to configure and set up the WhatsApp Business API on your server.

4. **Set up environment variables:** Create a `.env` file and define the necessary environment variables, including your WhatsApp API credentials.

5. **Start the bot:**
   ```bash
   cd /src/python chat-bot.py
   ```

## Usage

- Users can send scripture references or questions to the bot via WhatsApp.
- The bot interprets the input and provides explanations or references from the supported scriptures.
- Customize the bot's responses and add additional scriptures as required within the code.

## Supported Scriptures

At present, the bot supports the following scriptures:

- []

## Contributing

Contributions to the **Bible_chatbot** project are encouraged. If you wish to contribute new features, add support for more scriptures, or make enhancements, please adhere to these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Create relevant tests if applicable.
5. Ensure that existing tests pass.
6. Commit your changes and push them to your fork.
7. Submit a pull request.

## License

This project is licensed under the [MIT] License - please refer to the [LICENSE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for further details.

## Contact

For inquiries or support, kindly reach out to [MART] via [agentmart100@gmail.com].