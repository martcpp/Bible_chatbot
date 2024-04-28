import asyncio
from bibleAI import bible_verse
from versegen import *
from bot.twitterbot import create_tweet_dv, create_tweet_ep, create_tweet_pp


async def main():
    text_reference, version, reference = get_daily_verse()

    explanation, prayer = bible_verse(text_reference)

    await create_tweet_dv(text_reference, version, reference)
    await asyncio.sleep(120)  # Wait for 2 minutes
    await create_tweet_ep(explanation)
    await asyncio.sleep(120)  # Wait for 2 minutes
    await create_tweet_pp(prayer)

if __name__ == "__main__":
    asyncio.run(main())
