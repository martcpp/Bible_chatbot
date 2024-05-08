# Daily Bible Verse bot

![GitHub](https://img.shields.io/github/license/martcpp/daily-bible-verse-twitter-bot)
![GitHub last commit](https://img.shields.io/github/last-commit/martcpp/daily-bible-verse-twitter-bot)

A Python script to automate posting daily Bible verses, explanations, and prayers on Twitter.

## Overview

This project aims to create a Twitter bot that automatically posts daily Bible verses along with explanations and prayers. It utilizes Python's asyncio library for asynchronous execution and interacts with the Twitter API for posting tweets.

## Features

- Generates a daily Bible verse reference.
- Retrieves the verse text, explanation, and prayer using external modules.
- Posts daily verse, explanation, and prayer as separate tweets.
- Introduces a delay between tweets to avoid hitting Twitter's rate limits.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/martcpp/Bible_chatbot.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up Twitter API credentials in `.env or rename .env-example to .env`.

4. Run the script:

    ```bash
    python main.py
    ```

## Configuration

- `.env`: Contains Twitter API credentials. Replace placeholders with your actual credentials.


# Daily Bible Verse Twitter Bot Dockerized

This Dockerized Python script automatically posts daily Bible verses, explanations, and prayers on Twitter.

## Usage

### 1. Clone the Repository

Clone the repository to your local machine:

```
git clone https://github.com/your_username/daily-bible-verse-twitter-bot-dockerized.git
```

### 3. Build the Docker Image

Build the Docker image using the provided Dockerfile:

```
cd BIBLE_CHATBOT
docker build -t daily-bible-bot .
```

### 4. Run the Docker Container

Run the Docker container with the following command:

```
docker run -d daily-bible-bot
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the creators of the `tweepy` and `meta ai api` modules for providing the functionality to generate Bible verses and explanations.
- Special thanks to [Twitter](https://twitter.com) for providing the API to interact with the platform.

## Contact

For any questions or suggestions, feel free to contact the project maintainer:

Your Name  
Email: mordecaiemmanueletukudo@gmail.com  
Twitter: [@biblebot](https://twitter.com/BibleBotAI)

