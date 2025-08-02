#import tweepy
from tweepy.asynchronous import AsyncClient
from decouple import config

bearer_token = config('BEARER_TOKEN')
consumer_key = config('CONSUMER_KEY')
consumer_secret = config('CONSUMER_SECRET')
access_token = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')

# Initialize the async Tweepy client
client = AsyncClient(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

# me = await client.get_me()
# # Print the user's username
# print(f"Authenticated as: {me.data}")


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


if __name__ == "__main__":
    # Example usage
    import asyncio

    async def main():
        await create_tweet_dv("For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future.", "Jeremiah 29:11", "NIV")
        await asyncio.sleep(120)  # Wait for 2 minutes
        await create_tweet_ep("This is an explanation of the verse.")
        await asyncio.sleep(120)  # Wait for 2 minutes
        await create_tweet_pp("This is a prayer point related to the verse.")
        print("Twitter bot is ready to use.")
        
        me = await client.get_me()
        # Print the user's username
        print(f"Authenticated as: {me.data}")
    asyncio.run(main())