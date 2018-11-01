import discord
import asyncio
import time
import sys
import json
import random
from meme_images_dict import memes

config_data = json.load(open('config.json'))

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready")

def check(msg):
    if msg.channel.id == '1':
        return False
    return True

@client.event
async def on_message(message):
    if check(message):
        """if message.author.id == "168877392729866240":
            await client.delete_message(message)
            await client.send_message(message.channel, "sorry, you can't talk right now")
            """
        if message.content in memes:
            await client.send_file(message.channel, memes.get(message.content))
        elif message.content =="*okhand":
            string = "*okhand"
            r = random.randint(1,7)
            randomOk = string+str(r)
            await client.send_file(message.channel, memes.get(randomOk))
        elif message.author.id == "142425531801927680" and message.content == "*restart":
            await client.close()
            sys.exit(0)

client.run(config_data['access_token'])
