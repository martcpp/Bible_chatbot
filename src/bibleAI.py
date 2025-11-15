from meta_ai_api import MetaAI
from openai import OpenAI
from groq import Groq
from google import genai
import os
import time
from decouple import config
from utills import fallback_response, logger_setup, check_quotes

api_key = config("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


logger = logger_setup()

# Fallback response for when AI generation fails
fall_back = fallback_response()


def get_ai_response(prompt, max_retries=3, retry_delay=1):
    """Get AI response with retry logic"""
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",  #"gemini-2.5-pro",
                contents= prompt
            )
            if response.text:
                return response.text
            logger.error(f"Invalid response format, attempt {attempt + 1}")
        except Exception as e:
            logger.error(f"API error on attempt {attempt + 1}: {e}")

        if attempt < max_retries - 1:
            time.sleep(retry_delay)

    logger.error("All retry attempts failed")
    return None


def bible_verse(verse):
    """Generate bible verse explanation and prayer with optimizations"""

    # Primary prompts - more spiritual and engaging
    explanation_prompt = f"""Write a powerful, heart-touching explanation of "{verse}" that makes people feel God's love personally. Connect it to real-life struggles, speak with warmth and hope, make it deeply encouraging and relatable. Use simple but profound language that touches both heart and soul. Keep it under 270 characters and make people want to share it. with some nice hashtags."""
    prayer_prompt = f"""faith filled, spirit filled prayer based on "{verse}" that people can declare over their lives with confidence. Make it specific, personal, and powerful - like speaking directly to God as a loving Father. Include breakthrough, blessing, and transformation. Write it as a declaration of faith under 270 characters that builds expectation for God's goodness."""

    # Backup shorter prompts
    short_explanation = f"""Explain "{verse}" in a way that makes people feel God's personal love and care for them. Make it encouraging, hopeful, and relatable to daily life. Use warm, simple language that touches the heart. Under 260 characters. with some nice hashtags."""
    short_prayer = f"""Write a powerful prayer from "{verse}" that people can pray with bold faith. Make it personal, specific, and full of expectation for God's goodness. Under 260 characters."""

    # Get initial responses
    explanation = get_ai_response(explanation_prompt)
    prayer_point = get_ai_response(prayer_prompt)

    if not explanation or not prayer_point:
        logger.warning("Failed to get AI response, returning fallback")
        return fall_back["Explanation"], fall_back["Prayer"]

    exp_text = check_quotes(explanation)
    prayer_text = check_quotes(prayer_point)

    # Check if content is too long and retry with shorter prompts
    if len(exp_text) > 280 or len(prayer_text) > 280:
        if len(exp_text) > 280:
            explanation = get_ai_response(short_explanation)
            if explanation:
                exp_text = check_quotes(explanation)

        if len(prayer_text) > 272:
            prayer_point = get_ai_response(short_prayer)
            if prayer_point:
                prayer_text = check_quotes(prayer_point)

    # Final length check
    if len(exp_text) > 280:
        exp_text = fall_back["Explanation"]
    if len(prayer_text) > 280:
        prayer_text = fall_back["Prayer"]
    return exp_text, prayer_text


if __name__ == "__main__":
    verse = "For God so loved the world that whoever believes in him will not perish but have everlasting life. - John 3:16 - NIV"
    explanation, prayer = bible_verse(verse)
    print("Explanation1:", explanation)
    print("Prayer1:", prayer)

    verse = "For God so loved the world that whoever believes in him will not perish but have everlasting life. - John 3:16 - NIV"
    explanation, prayer = bible_verse(verse)
    print("Explanation2:", explanation)
    print("Prayer2:", prayer)
    
    # resp = client.models.generate_content(
    #     model="gemini-2.5-pro",
    #     contents= verse
    # )
    # print(resp.text)