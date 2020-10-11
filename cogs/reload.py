import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os


class reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # reload command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_owner()
    async def reload(self, ctx):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                self.bot.unload_extension(f'cogs.{filename[:-3]}')
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                self.bot.load_extension(f'cogs.{filename[:-3]}')
        embedVar = discord.Embed(title=':white_check_mark: Successfully reloaded cogs.', color=0x7289da)
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(reload(bot))