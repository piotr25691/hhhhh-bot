import discord
import re
from discord.ext import commands
from discord.ext.commands import bot
from vars import *

class fix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="statusfix")
    @commands.is_owner()
    async def fix(self, ctx):
        activity = discord.Activity(type=discord.ActivityType.streaming, name=f"h | Use hh!help | {version}",
                                    url="https://www.youtube.com/watch?v=DwjbP7aihxQ")
        await self.bot.change_presence(status='dnd', activity=activity)
        return await ctx.send(":white_check_mark: Status has been re-set.")

def setup(bot):
    bot.add_cog(fix(bot))