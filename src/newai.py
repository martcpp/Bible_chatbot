from meta_ai_api import MetaAI

ai = MetaAI()

def bible_verse(verse):
    # Much better, more spiritual and engaging prompts
    explanation_text = f"""Write a powerful, heart-touching explanation of "{verse}" that makes people feel God's love personally. Connect it to real-life struggles, speak with warmth and hope, make it deeply encouraging and relatable. Use simple but profound language that touches both heart and soul. Keep it under 280 characters and make people want to share it."""
    
    prayer_text = f"""Create a bold, faith-filled prayer based on "{verse}" that people can declare over their lives with confidence. Make it specific, personal, and powerful - like speaking directly to God as a loving Father. Include breakthrough, blessing, and transformation. Write it as a declaration of faith under 280 characters that builds expectation for God's goodness."""
    
    # Backup prompts if first ones are too long
    explanation_2 = f"""Explain "{verse}" in a way that makes people feel God's personal love and care for them. Make it encouraging, hopeful, and relatable to daily life. Use warm, simple language that touches the heart. Under 270 characters."""
    
    prayer_text_2 = f"""Write a powerful prayer from "{verse}" that people can pray with bold faith. Make it personal, specific, and full of expectation for God's goodness. Under 270 characters."""
    
    explanation = ai.prompt(message=explanation_text)
    prayer_point = ai.prompt(message=prayer_text)
    
    if explanation is not None and prayer_point is not None:
        explen = len(explanation['message'])
        praylen = len(prayer_point['message'])
        print(f"explanation length:{explen} praylen:{praylen}")
        
        if explen > 280 or praylen > 280:
            print("explanation or prayer point is too long, trying shorter prompts")
            explanation = ai.prompt(message=explanation_2)
            prayer_point = ai.prompt(message=prayer_text_2)
    
    print(explanation['message'])
    print("-----------------------------------")
    print(prayer_point['message'])
    return explanation['message'], prayer_point['message']

if __name__ == "__main__":
    verse = "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future. - Jeremiah 29:11"
    explanation, prayer = bible_verse(verse)
    print(f"Explanation: {explanation}")
    print(f"Prayer Point: {prayer}")
    print(f"Explanation Length: {len(explanation)}")
    print(f"Prayer Point Length: {len(prayer)}")