import os
from pyzoom import ZoomClient
from datetime import datetime as dt
from discord.ext import commands

KEY = os.getenv('key')
SECRET = os.getenv('secret')
client = ZoomClient('9LUet6aOQxOTRAUtAteRWQ', 'CuKFaXw6s4NSJTyZwyIzICOyoE7iX7K8nEM0')
print(KEY)

bot = commands.Bot(command_prefix='$', help_command=None)
prefix = '$'

@bot.event
async def on_message(message):

    await bot.process_commands(message)

    if message.content.startswith("{}meeting".format(prefix)):

        res = client.meetings.create_meeting(topic='test', start_time=dt.now().isoformat(), duration_min=60)
        meeting = str(res)
        array = meeting.split(" ")
        link = array[9].split("'")[1]
        await message.channel.send(link)

with open("TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print('connected')
    bot.run(TOKEN)