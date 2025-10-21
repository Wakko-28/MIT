from dotenv import load_dotenv
from openai import OpenAI
import os
import time

# Load environment variables
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=OPENAI_KEY)

# You can still store your assistant ID if you want to use a specific model or config
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

# Create a simple response (equivalent to your original flow)
response = client.responses.create(
    model="gpt-4.1-mini",  # or "gpt-4.1" if you want the full version
    input="Hi Don pez!,que fecha es hoy?"
)

# Extract and print the assistant’s text output
print(response.output[0].content[0].text)
