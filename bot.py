import discord
from discord.ext import commands

import json
import random
import os

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='f!')

@bot.event
async def on_ready():
    print(">>Bot is online<<")
#進入
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['welcomechannel']))
    await channel.send(f'{member}-沒朋友怪進來了喔!')
    print(f'{member}join!')
#離開
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['leavechannel']))
    await channel.send(f'{member}-有朋友快滾!')
    print(f'{member}leave!')

For Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cmds.{Filename[:-3]}')

if __name__ == "__main__":

bot.run(jdata['TOKEN'])    