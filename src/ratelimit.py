from decouple import config
import tweepy
from tweepy.errors import TooManyRequests
import time
import os


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
# Initialize the async Tweepy client'


client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

# me = client.get_me()
# print(f"Authenticated as: {me}")

try:
    limit = client.create_tweet(text="asynchronous")
    print(f"Rate limit status: {limit}")
except TooManyRequests as e:
    print(f"Rate limit exceeded: {e}")
    # fake = e.response.Headers()
    # print(f"Rate limit reset time: {fake}")
    time_t = e.response.headers.get("x-rate-limit-reset")
    print(f"Rate limit will reset at: {time_t}")

    now_time = int(time.time())
    wait_time = int(time_t) - now_time
    print(f"Waiting for {wait_time} seconds before retrying...")

    print("Rate limit status:")
    print(f"  Limit: {e.response.headers.get('x-rate-limit-limit')}")
    print(f"  Remaining: {e.response.headers.get('x-rate-limit-remaining')}")
    print(f"  Reset: {e.response.headers.get('x-rate-limit-reset')}")

# timej = 1754228366
# convert = int(timej)
# print(f"Converted time: {convert}")

# current_time = int(time.time())
# print(f"Current time: {current_time}")

# print("x UTC:", time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(convert)))
# print("x WAT:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(convert)))

# print("current UTC:", time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(current_time)))
# print("current WAT:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time)))
# wait_time = current_time - convert  # 1 minute in seconds
# print(f"Waiting for {wait_time} seconds...")
# wait_time = max(wait_time, 60)
# print(f"Adjusted wait time: {wait_time} seconds")
