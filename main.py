import discord
import asyncio
import time
import sys
import json
#import pathlib from Path #used to handle windows / characters in file names
from meme_images_dict import memes

config_data = json.load(open('config.json'))

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready")
    print(memes)

@client.event
async def on_message(message):
    if message.content in memes:
        await client.send_file(message.channel, memes.get(message.content))

    elif message.author.id == "142425531801927680" and message.content == "*restart":
        await client.close()
        sys.exit(0)

client.run(config_data['access_token'])
# things to consider:
#meme_images_dict to search for images

