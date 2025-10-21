from dotenv import load_dotenv
from openai import OpenAI
import discord
import os

# Load environment variables
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")
DISCORD_TOKEN = os.getenv("TOKEN")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

# --- OpenAI setup ---
openai_client = OpenAI(api_key=OPENAI_KEY)

# --- Discord setup ---
intents = discord.Intents.default()
intents.message_content = True  # Needed to read messages

discord_client = discord.Client(intents=intents)

@discord_client.event
async def on_ready():
    print(f'✅ Bot logged in as {discord_client.user}')

@discord_client.event
async def on_message(message):
    # Ignore the bot's own messages
    if message.author == discord_client.user:
        return

    # Optional: add a prefix to trigger (e.g. "!ask")
    if message.content.startswith(""):
        user_input = message.content[len(""):]

        # Send typing indicator
        async with message.channel.typing():
            try:
                # Create a response using the new Responses API
                response = openai_client.responses.create(
                    model="gpt-4.1-mini",
                    input=user_input
                    # You can also add: assistant_id=ASSISTANT_ID
                )

                # Extract text from the response
                reply = response.output[0].content[0].text

                # Send back to Discord
                await message.channel.send(reply)

            except Exception as e:
                await message.channel.send(f"⚠️ Error: {e}")

# Run the Discord bot
discord_client.run(DISCORD_TOKEN)
