import asyncio
from bibleAI import bible_verse
from versegen import *
from bot.twitterbot import create_tweet_dv, create_tweet_ep, create_tweet_pp


async def main():
    text_reference, version, reference = get_daily_verse()
    verser = f"{text_reference} - {version} - {reference}"

    explanation, prayer = bible_verse(verser)

    await create_tweet_dv(text_reference, version, reference)
    await asyncio.sleep(30)  # Wait for 30 seconds
    await create_tweet_ep(explanation)
    await asyncio.sleep(30)  # Wait for 30 seconds
    await create_tweet_pp(prayer)

if __name__ == "__main__":
    asyncio.run(main())
