import discord
import time
from discord.ext import commands


class ping(commands.Cog):
    # ping command
    def __init__(self, client):
      self.client = client
    @commands.command(name='pinq')
    async def ping(self, ctx):
      async with ctx.channel.typing():
        t1 = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        res = round((t2-t1)*1000) 
      await ctx.send(embed=discord.Embed(title=":ping_pong: Ponq!", description=f":white_small_square: Bot Latency: **{round(self.client.latency*1000)}**ms\n:white_small_square: API Latency: **{res}**ms", colour=discord.Colour.blurple()))

        
        

def setup(client):
    client.add_cog(ping(client))