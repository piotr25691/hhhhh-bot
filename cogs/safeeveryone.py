import discord
from discord.ext import commands

class safeeveryone(commands.Cog):
    # safeeveryone command
    @commands.command(aliases=['pinqeveryone', 'ateveryone'])
    async def everyonepinq(self, ctx):
        await ctx.message.delete()
        # define an embed with @everyone
        embedVar = discord.Embed(description='@everyone', color=0x7289da)
        # send the embed
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(safeeveryone(bot))