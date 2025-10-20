from dotenv import load_dotenv
import discord
import os

# load enviroment variables from .env file
load_dotenv()

#set up intents 
intents = discord.Intents.default() 
intents.message_content = True  # Ensure that your bot can read message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  Print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
        
