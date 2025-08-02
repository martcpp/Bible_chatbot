def fallback_response():
    """Return a fallback response in case of API failure"""
    fall_back_message = {
        "Explanation": "This verse reminds us not to worry. Instead, talk to God about everything with gratitude. Trust Him with your needs and He'll give you peace beyond understanding.",
        "Prayer": "Even Jesus made personal supplications: Lord, I give You my worries. Teach me to trust You more each day. Help me to pray with faith and gratitude. I choose peace over panic, knowing You're in control. Amen.",
        "Verse": "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God.",
        "Version": "NIV",
        "Reference": "Philippians 4:6"
    }

    return fall_back_message


# if __name__ == "__main__":
#     print(fallback_response())
#     print("Fallback response printed successfully.")
#     exp = fallback_response()['Explanation']
#     pray = fallback_response()['Prayer']
#     verse = fallback_response()['Verse']
#     version = fallback_response()['Version']
#     reference = fallback_response()['Reference']
#     print(f"Verse: {verse} - {version} - {reference}")
#     print(f"Explanation: {exp}")
#     print(f"Prayer: {pray}")
    
#     for key, value in fallback_response().items():
#         print(f"{key}: {len(value)} characters")

