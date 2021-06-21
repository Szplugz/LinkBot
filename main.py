import os
import time
from dotenv import load_dotenv
from pyzoom import ZoomClient
from datetime import datetime as dt
from discord.ext import commands

load_dotenv()
KEY = os.getenv('key')
SECRET = os.getenv('secret')
client = ZoomClient(KEY, SECRET)

bot = commands.Bot(command_prefix='$', help_command=None)
prefix = '$'

# @bot.event
# async def on_message(message):

#     await bot.process_commands(message)

#     if message.content.startswith("{}meeting".format(prefix)):

#         res = client.meetings.create_meeting(topic='test', start_time=dt.now().isoformat(), duration_min=60)
#         meeting = str(res)
#         array = meeting.split(" ")
#         link = array[9].split("'")[1]
#         await message.channel.send(link)

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

with open("TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print('connected')
    bot.run(TOKEN)