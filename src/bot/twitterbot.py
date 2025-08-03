import os
from tweepy.asynchronous import AsyncClient
from decouple import config
from utills import logger_setup
import asyncio
from tweepy.errors import TooManyRequests
import time

# # Setup logger
logger = logger_setup()





# Ensure all required environment variables are set
bearer_token = config("BEARER_TOKEN") or os.getenv("BEARER_TOKEN")
if not bearer_token:
    raise ValueError("BEARER_TOKEN is not set in environment variables or .env file")
consumer_key = config("CONSUMER_KEY") or os.getenv("CONSUMER_KEY")
if not consumer_key:
    raise ValueError("CONSUMER_KEY is not set in environment variables or .env file")
consumer_secret = config("CONSUMER_SECRET") or os.getenv("CONSUMER_SECRET")
if not consumer_secret:
    raise ValueError("CONSUMER_SECRET is not set in environment variables or .env file")
access_token = config("ACCESS_TOKEN") or os.getenv("ACCESS_TOKEN")
if not access_token:
    raise ValueError("ACCESS_TOKEN is not set in environment variables or .env file")
access_token_secret = config("ACCESS_TOKEN_SECRET") or os.getenv("ACCESS_TOKEN_SECRET")
if not access_token_secret:
    raise ValueError(
        "ACCESS_TOKEN_SECRET is not set in environment variables or .env file"
    )

# Initialize the async Tweepy client
client = AsyncClient(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)


async def create_tweet_safely(client, text,max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Attempt {attempt} to create tweet...")
            return await client.create_tweet(text=text)
        
        except TooManyRequests as e:
            reset_timestamp = e.response.headers.get("x-rate-limit-reset")
            current_timestamp = int(time.time())

            if reset_timestamp:
                wait_time = int(reset_timestamp) - current_timestamp
            else:
                wait_time = attempt * 60  # fallback to increasing wait time

            wait_time = max(wait_time, 60)
            logger.warning(f"Rate limit hit, waiting {wait_time} seconds before retrying...")
            await asyncio.sleep(wait_time)

        except Exception as e:
            logger.error(f"Unexpected error on attempt {attempt}: {e}")
            break

    logger.error("All attempts to tweet failed.")
    return None



async def create_tweet_dv(text, verse, reference):
    # Use await when calling asynchronous methods
    post = f"{text} \n {reference} - {verse}"
    response = await create_tweet_safely(client, post)
    logger.info(f"Tweet created: https://twitter.com/user/status/{response.data['id']}")


async def create_tweet_ep(text):
    # Use await when calling asynchronous methods
    post = f"{text} #explanation"
    response = await create_tweet_safely(client, post)
    logger.info(f"Tweet created: https://twitter.com/user/status/{response.data['id']}")


async def create_tweet_pp(text):
    # Use await when calling asynchronous methods
    post = f"{text} #prayer"
    response = await create_tweet_safely(client, post)
    logger.info(f"Tweet created: https://twitter.com/user/status/{response.data['id']}")

