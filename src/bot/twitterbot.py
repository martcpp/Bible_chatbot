import tweepy
import tweepy.asynchronous
from decouple import config


consumer_key = config('CONSUMER_KEY')
consumer_secret = config('CONSUMER_SECRET')
access_token = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')

# Initialize the async Tweepy client
client = tweepy.asynchronous.AsyncClient(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


async def create_tweet_dv(text, verse, reference):
    # Use await when calling asynchronous methods
    response = await client.create_tweet(
        text=f"{text} \n {verse} - {reference}"
    )
    print(response)
    print(f"https://twitter.com/user/status/{response.data['id']}")


async def create_tweet_ep(text):
    # Use await when calling asynchronous methods
    response = await client.create_tweet(
        text=f"{text} #dailyverse #bibleverse"
    )
    print(response)
    print(f"https://twitter.com/user/status/{response.data['id']}")


async def create_tweet_pp(text):
    # Use await when calling asynchronous methods
    response = await client.create_tweet(
        text=f"{text} #prayerpoint"
    )
    print(response)
    print(f"https://twitter.com/user/status/{response.data['id']}")
