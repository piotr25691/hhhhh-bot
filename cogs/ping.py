import discord
from discord.ext import commands
from discord.ext.commands import Bot

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # ping command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pinq(self, ctx):
        # ping the bot and return the time it took to ping in chat
        await ctx.message.delete()
        embedVar = discord.Embed(description=f'**Ponq!** {round(self.bot.latency * 1000, 1)}ms', color=0x00ff00)
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(ping(bot))