from dotenv import load_dotenv
import discord
import os
import logging

# load environment variables from .env file
load_dotenv()

# basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# set up intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure that your bot can read message content (enable in Developer Portal)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logger.info(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # ignore messages from ourselves and other bots
    if message.author == client.user or getattr(message.author, "bot", False):
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

if __name__ == '__main__':
    # Look for common env var names and validate
    token = os.getenv('TOKEN') or os.getenv('DISCORD_TOKEN')
    if not token:
        logger.error('Discord token not found in environment. Set TOKEN or DISCORD_TOKEN in your .env or environment.')
        raise SystemExit('Discord token not found. Aborting.')
    client.run(token)
