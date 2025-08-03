import requests
from decouple import config
from utills import fallback_response, logger_setup
import os


# Create logger
logger = logger_setup()

base_url = (
    config("BASE_URL") + "format={}&order={}"
    or os.getenv("BASE_URL") + "format={}&order={}"
)
if not base_url:
    raise ValueError("BASE_URL is not set in environment variables or .env file")

format_param = config("FORMAT") or os.getenv("FORMAT")
if not format_param:
    raise ValueError("FORMAT is not set in environment variables or .env file")
order_param = config("ORDER") or os.getenv("ORDER")
if not order_param:
    raise ValueError("ORDER is not set in environment variables or .env file")

# Format the URL with the parameters
url = base_url.format(format_param, order_param)
fall_back = fallback_response()


def get_daily_verse():
    logger.info("Starting daily verse fetch")
    logger.debug(f"Fetching from URL: {url}")

    try:
        response = requests.get(url, timeout=10)
        logger.info(f"API response received with status code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()

            if "verse" in data and "details" in data["verse"]:
                logger.info("Verse details found in the response")
                verse_details = data["verse"]["details"]

                if verse_details:
                    # Safely get values with fallback to empty string
                    text_reference = verse_details.get("text", "").strip()
                    version = verse_details.get("version", "").strip()
                    reference = verse_details.get("reference", "").strip()

                    # Check if any required field is missing
                    if not all([text_reference, version, reference]):
                        logger.warning(
                            "Missing required verse data, using fallback response"
                        )
                        return (
                            fall_back["Verse"],
                            fall_back["Version"],
                            fall_back["Reference"],
                        )

                    total_text_len = len(text_reference) + len(version) + len(reference)
                    # logger.debug(f"Character count - text: {len(text_reference)}, version: {len(version)}, reference: {len(reference)}")

                    if total_text_len > 280:
                        logger.warning(
                            f"Total characters ({total_text_len}) exceeds 280 limit, using fallback response"
                        )
                        return (
                            fall_back["Verse"],
                            fall_back["Version"],
                            fall_back["Reference"],
                        )

                    return text_reference, version, reference
                else:
                    logger.warning(
                        "Empty verse details received, using fallback response"
                    )
                    return (
                        fall_back["Verse"],
                        fall_back["Version"],
                        fall_back["Reference"],
                    )
            else:
                logger.warning(
                    "No verse details found in API response, using fallback response"
                )
                logger.debug(
                    f"Response structure: {list(data.keys()) if isinstance(data, dict) else 'Not a dict'}"
                )
                return fall_back["Verse"], fall_back["Version"], fall_back["Reference"]
        else:
            logger.error(f"API request failed with HTTP {response.status_code}")
            return fall_back["Verse"], fall_back["Version"], fall_back["Reference"]

    except requests.exceptions.Timeout:
        logger.error("Request timed out after 10 seconds")
        return fall_back["Verse"], fall_back["Version"], fall_back["Reference"]
    except requests.exceptions.ConnectionError:
        logger.error("Connection error occurred while fetching verse")
        return fall_back["Verse"], fall_back["Version"], fall_back["Reference"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return fall_back["Verse"], fall_back["Version"], fall_back["Reference"]
    except KeyError as e:
        logger.error(f"Missing key in fallback response: {str(e)}")
        logger.critical("Fallback response structure is invalid")
        return "Default verse", "Default version", "Default reference"
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}", exc_info=True)
        return fall_back["Verse"], fall_back["Version"], fall_back["Reference"]
