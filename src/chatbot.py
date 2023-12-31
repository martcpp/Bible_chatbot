import openai
import os
from dotenv import load_dotenv


load_dotenv()
# Set your OpenAI API key
openai.api_key = os.getenv("open.API_KEY")

# Function to generate a response
def generate_response(user_input):
    """
    Generates a response to the user's input using the OpenAI GPT-3.5-Turbo model.

    Args:
        user_input (str): The user's input to generate a response to.

    Returns:
        str: The response generated by the GPT-3.5-Turbo model.
    """
    prompt = user_input + "\nbible chatbot:\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.15,
            max_tokens=1500  # Adjust the token limit as needed
        )
        
        return response.choices[0].message["content"].strip()

    except Exception as e:
        return str(e)

