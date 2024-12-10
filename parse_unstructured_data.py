#parse unstructured data using OpenAI API
# USE openairag virtual environment to execute this program
# the .env file has the OPENAI_API_KEY variable
# Text is parsed into CSV format
import os
import openai
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY=""

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{"role": "user", "content": "What is IBM APIC"}],
    temperature=0,
    max_tokens=256
)
print(response)