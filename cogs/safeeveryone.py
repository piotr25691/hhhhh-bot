import discord
from discord.ext import commands

class safeeveryone(commands.Cog):
    # safeeveryone command
    @commands.command(aliases=['pinqeveryone', 'ateveryone'])
    async def everyonepinq(self, ctx):
        await ctx.message.delete()
        # define an embed with @everyone
        e = discord.Embed(description='@everyone', color=discord.Colour.blurple())
        # send the embed
        await ctx.send(embed=e)

def setup(client):
    client.add_cog(safeeveryone(client))