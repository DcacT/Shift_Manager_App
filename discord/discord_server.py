import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Bot setup

TOKEN = 'token' 

intents = discord.Intents.default()
# intents.message_content = True  # Ensure this is enabled in the Developer Portal

monitored_message_list = []

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content[0] == '!':
        print(f'command {message.content} from {message.author.display_name}')
        return 

@client.event
async def on_raw_reaction_add(payload):
    print(f'reaction "{payload.emoji.name}" added on message: {payload.message_id} by {payload.user_id}')

@client.event
async def on_raw_reaction_remove(payload):
    print(f'reaction "{payload.emoji.name}" removed on message: {payload.message_id} by {payload.user_id}')

client.run(TOKEN)
