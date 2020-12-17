import discord
from discord.ext import commands
from vars import *

class say(commands.Cog):
    # say command (g doesnt work, dont try)
    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def say(self, ctx, *, body):
        await ctx.send(body)

def setup(client):
    client.add_cog(say(client))