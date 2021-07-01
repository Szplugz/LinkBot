import os
import time
import json
from dotenv import load_dotenv
from pyzoom import ZoomClient
from datetime import datetime as dt
from discord.ext import commands

load_dotenv()
KEY = os.getenv('key')
SECRET = os.getenv('secret')
TOKEN = os.getenv('token')
client = ZoomClient(KEY, SECRET)

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix, help_command=None)

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '$'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command(name="changeprefix")
async def change_prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'prefix changed to: {prefix}')

@bot.command(name="new")
async def new(ctx, arg):

    if arg == "zoom".lower():
        await ctx.send("Generating zoom meeting link")
        time.sleep(2)
        res = client.meetings.create_meeting(topic='test', start_time=dt.now().isoformat(), duration_min=60)
        meeting = str(res)
        array = meeting.split(" ")
        link = array[9].split("'")[1]
        await ctx.send(link)

    if arg == "gmeet".lower():
        await ctx.send("http://meet.google.com/new")

bot.run(TOKEN)