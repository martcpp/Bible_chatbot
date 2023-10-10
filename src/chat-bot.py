import openai
import os
from dotenv import load_dotenv


load_dotenv()
# Set your OpenAI API key
openai.api_key = os.getenv("open.API_KEY")

# Function to generate a response
def generate_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.15,
            max_tokens=1500  # Adjust the token limit as needed
        )

        return response.choices[0].message["content"].strip()

    except Exception as e:
        return str(e)

# Main loop to interact with the user
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        prompt = user_input + "\nbible chatbot:\n"
        # Exit the loop if the user enters "exit" or "quit"
        if user_input.lower() in ["exit", "quit"]:
            break
        
        response = generate_response(user_input)
        print("bible bot:", response)
