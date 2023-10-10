import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("open.API_KEY")


import openai

def Bible_chatbot(prompt):
    """
    Generates a response to the given prompt using OpenAI's text-davinci-002 engine.

    Args:
        prompt (str): The prompt to generate a response for.

    Returns:
        str: The generated response.
    """
  
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50  # Adjust this value to limit the length of the generated text
    )

    generated_text = response.choices[0].text
    
    return generated_text


if __name__ == "__main__":
    start = input("enter your search ") 
    prompt = start
    response = Bible_chatbot(prompt)
    print(response)
  