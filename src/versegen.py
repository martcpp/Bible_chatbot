import requests
from decouple import config
from bot.twitterbot import *
from bibleAI import *


# Define the base URL with placeholders for parameters
base_url = config('BASE_URL')+"format={}&order={}"

# Define the parameters
format_param = "json"
order_param = "daily"

# Format the URL with the parameters
url = base_url.format(format_param, order_param)


def get_daily_verse():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        verse_details = data["verse"]["details"]

        text_reference = verse_details["text"]
        version = verse_details["version"]
        reference = verse_details["reference"]

        print(f"{text_reference} - {version} - {reference}")

        return text_reference, version, reference
    else:
        print("Failed to fetch data:", response.status_code)


if __name__ == "__main__":
    get_daily_verse()