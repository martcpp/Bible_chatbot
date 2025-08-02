import requests
import logging
from datetime import datetime
from decouple import config
from bot.twitterbot import *
from bibleAI import *
from utills import fallback_response

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bible_verse_fetcher.log'),
        logging.StreamHandler()
    ]
)

# Create logger
logger = logging.getLogger(__name__)

base_url = config('BASE_URL') + "format={}&order={}"

format_param = config('FORMAT')
order_param = config('ORDER')

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
            logger.debug(f"Response data: {data}")
            
            if "verse" in data and "details" in data["verse"]:
                logger.info("Verse details found in the response")
                verse_details = data["verse"]["details"]
                logger.debug(f"Verse details: {verse_details}")
                
                if verse_details:
                    # Safely get values with fallback to empty string
                    text_reference = verse_details.get("text", "").strip()
                    version = verse_details.get("version", "").strip()
                    reference = verse_details.get("reference", "").strip()
                    
                    # Check if any required field is missing
                    if not all([text_reference, version, reference]):
                        logger.warning("Missing required verse data, using fallback response")
                        logger.debug(f"Missing data - text: {bool(text_reference)}, version: {bool(version)}, reference: {bool(reference)}")
                        return fall_back['Verse'], fall_back['Version'], fall_back['Reference']
                    
                    total_text_len = len(text_reference) + len(version) + len(reference)
                    logger.debug(f"Character count - text: {len(text_reference)}, version: {len(version)}, reference: {len(reference)}")
                    
                    if total_text_len > 280:
                        logger.warning(f"Total characters ({total_text_len}) exceeds 280 limit, using fallback response")
                        return fall_back['Verse'], fall_back['Version'], fall_back['Reference']
                    
                    logger.info(f"Successfully fetched verse. Total characters: {total_text_len}")
                    logger.debug(f"Verse reference: {reference}")
                    return text_reference, version, reference
                else:
                    logger.warning("Empty verse details received, using fallback response")
                    return fall_back['Verse'], fall_back['Version'], fall_back['Reference']
            else:
                logger.warning("No verse details found in API response, using fallback response")
                logger.debug(f"Response structure: {list(data.keys()) if isinstance(data, dict) else 'Not a dict'}")
                return fall_back['Verse'], fall_back['Version'], fall_back['Reference']
        else:
            logger.error(f"API request failed with HTTP {response.status_code}")
            logger.debug(f"Response content: {response.text}")
            return fall_back['Verse'], fall_back['Version'], fall_back['Reference']
            
    except requests.exceptions.Timeout:
        logger.error("Request timed out after 10 seconds")
        return fall_back['Verse'], fall_back['Version'], fall_back['Reference']
    except requests.exceptions.ConnectionError:
        logger.error("Connection error occurred while fetching verse")
        return fall_back['Verse'], fall_back['Version'], fall_back['Reference']
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return fall_back['Verse'], fall_back['Version'], fall_back['Reference']
    except KeyError as e:
        logger.error(f"Missing key in fallback response: {str(e)}")
        logger.critical("Fallback response structure is invalid")
        return "Default verse", "Default version", "Default reference"
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}", exc_info=True)
        return fall_back['Verse'], fall_back['Version'], fall_back['Reference']


if __name__ == "__main__":
    logger.info("=== Bible Verse Fetcher Started ===")
    
    try:
        text_reference, version, reference = get_daily_verse()
        
        logger.info("Successfully retrieved verse data")
        logger.info(f"Reference: {reference}")
        logger.info(f"Version: {version}")
        logger.debug(f"Text length: {len(text_reference)} characters")
        
        print(f"Text Reference: {text_reference}")
        print(f"Version: {version}") 
        print(f"Reference: {reference}")
        
        # Uncomment when ready to use
        # logger.info("Calling AI services for explanation and prayer")
        # explanation, prayer = bible_verse(text_reference)
        # logger.info("AI services completed successfully")
        # logger.debug(f"Explanation length: {len(explanation)} characters")
        # logger.debug(f"Prayer length: {len(prayer)} characters")
        # print(f"Explanation: {explanation}")
        # print(f"Prayer Point: {prayer}")
        
    except Exception as e:
        logger.critical(f"Critical error in main execution: {str(e)}", exc_info=True)
        print("A critical error occurred. Check the logs for details.")
    
    logger.info("=== Bible Verse Fetcher Completed ===")