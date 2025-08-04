import logging
import os
import inspect


def fallback_response():
    """Return a fallback response in case of API failure"""
    fall_back_message = {
        "Explanation": "This verse reminds us not to worry. Instead, talk to God about everything with gratitude. Trust Him with your needs and He'll give you peace beyond understanding.",
        "Prayer": "Even Jesus made personal supplications: Lord, I give You my worries. Teach me to trust You more each day. Help me to pray with faith and gratitude. I choose peace over panic, knowing You're in control. Amen.",
        "Verse": "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God.",
        "Version": "NIV",
        "Reference": "Philippians 4:6",
    }

    return fall_back_message


def logger_setup():
    """Setup logging configuration using caller’s file name as logger name"""

    # Get the name of the file that called this function (not utils.py)
    caller_frame = inspect.stack()[1]
    caller_file_path = caller_frame.filename
    caller_file_name = os.path.basename(caller_file_path)

    logger = logging.getLogger(caller_file_name)
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler("../bible_ai.log")
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger


def check_quotes(text):
    """Check if text starts or ends with quotes and remove them"""
    if not text:
        return ""
    text = text.strip()
    if text.startswith('"'):
        text = text.strip('"')
    if text.endswith('"'):
        text = text.strip('"')
    return text
