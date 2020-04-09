import discord
from discord.ext import commands
from core.classes import Cog_Extension

import random
import json

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class react(Cog_Extension):
    #我就爛
    @commands.command()
    async def pic(self, ctx):
    random_pic = random.choice(jdata['picbad'])
    pic = discord.File(random_pic)
       await ctx.send(file = pic)    
def setup(bot):
    bot.add_cog(Main(bot))         