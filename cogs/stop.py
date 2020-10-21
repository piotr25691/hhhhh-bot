import discord
from discord.ext import commands
from discord.ext.commands import Bot
import sys


class stop(commands.Cog):
    # stop command
    @commands.command(aliases=['kill', 'die'])
    # check whether the bot owner tries to kill the bot from chat or not
    @commands.is_owner()
    async def terminate(self, ctx):
        # delete the message
        await ctx.message.delete()
        # stop execution
        await ctx.send(':white_check_mark: Stopped <@!742388119516741642>')
        sys.exit('bot has been stopped by bot owner')

def setup(bot):
    bot.add_cog(stop(bot))