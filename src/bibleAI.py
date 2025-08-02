from meta_ai_api import MetaAI
import time
from utills import fallback_response
ai = MetaAI()

def get_ai_response(prompt, max_retries=3, retry_delay=1):
    """Get AI response with retry logic"""
    for attempt in range(max_retries):
        try:
            response = ai.prompt(message=prompt)
            if response and 'message' in response:
                return response
            print(f"Invalid response format, attempt {attempt + 1}")
        except Exception as e:
            print(f"API error on attempt {attempt + 1}: {e}")
        
        if attempt < max_retries - 1:
            time.sleep(retry_delay)
    
    print("All retry attempts failed")
    return None

def bible_verse(verse):
    """Generate bible verse explanation and prayer with optimizations"""
    
    # Primary prompts - more spiritual and engaging
    explanation_prompt = f"""Write a powerful, heart-touching explanation of "{verse}" that makes people feel God's love personally. Connect it to real-life struggles, speak with warmth and hope, make it deeply encouraging and relatable. Use simple but profound language that touches both heart and soul. Keep it under 280 characters and make people want to share it."""
    
    prayer_prompt = f"""Create a bold, faith-filled prayer based on "{verse}" that people can declare over their lives with confidence. Make it specific, personal, and powerful - like speaking directly to God as a loving Father. Include breakthrough, blessing, and transformation. Write it as a declaration of faith under 280 characters that builds expectation for God's goodness."""
    
    # Backup shorter prompts
    short_explanation = f"""Explain "{verse}" in a way that makes people feel God's personal love and care for them. Make it encouraging, hopeful, and relatable to daily life. Use warm, simple language that touches the heart. Under 270 characters."""
    
    short_prayer = f"""Write a powerful prayer from "{verse}" that people can pray with bold faith. Make it personal, specific, and full of expectation for God's goodness. Under 270 characters."""
    
    # Get initial responses
    explanation = get_ai_response(explanation_prompt)
    prayer_point = get_ai_response(prayer_prompt)
    
    if not explanation or not prayer_point:
        print("Failed to get AI response, please try again")
        return None, None
    
    exp_text = explanation.get('message', '')
    prayer_text = prayer_point.get('message', '')
    
    print(f"Initial lengths - Explanation: {len(exp_text)}, Prayer: {len(prayer_text)}")
    
    # Check if content is too long and retry with shorter prompts
    if len(exp_text) > 280 or len(prayer_text) > 280:
        print("Content too long, trying shorter prompts...")
        
        if len(exp_text) > 280:
            explanation = get_ai_response(short_explanation)
            if explanation:
                exp_text = explanation.get('message', '')
            # exp_text = explanation.get('message', '') if explanation else exp_text
        
        if len(prayer_text) > 280:
            prayer_point = get_ai_response(short_prayer)
            if prayer_point:
                prayer_text = prayer_point.get('message', '')
            # prayer_text = prayer_point.get('message', '') if prayer_point else prayer_text

    # Final validation - truncate if still too long
    if len(exp_text) > 280:
        exp_text = fallback_response()['Explanation']
    if len(prayer_text) > 280:
        prayer_text = fallback_response()['Prayer']

    print(exp_text)
    print("-----------------------------------")
    print(prayer_text)
    
    return exp_text, prayer_text

if __name__ == "__main__":
    verse = "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future. - Jeremiah 29:11"
    explanation, prayer = bible_verse(verse)
    print(f"Explanation: {explanation}")
    print(f"Prayer Point: {prayer}")
    print(f"Explanation Length: {len(explanation)}")
    print(f"Prayer Point Length: {len(prayer)}")