import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("open.API_KEY")

