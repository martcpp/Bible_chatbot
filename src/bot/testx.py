from tweepy.asynchronous import AsyncClient
from decouple import config
import tweepy

bearer_token = config('BEARER_TOKEN')
consumer_key = config('API_KEY')
consumer_secret = config('API_SECRET')
access_token = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')

# Initialize the async Tweepy client

client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

me = client.get_me()
# Print the user's username
print(f"Authenticated as: {me}")