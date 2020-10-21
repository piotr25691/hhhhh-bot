import discord
from discord.ext import commands
from discord.ext.commands import Bot
import sys
import os


class stop(commands.Cog):
    # stop command
    @commands.command(aliases=['restart', 'reboot'])
    # check whether the bot owner tries to kill the bot from chat or not
    @commands.is_owner()
    async def restart_(self, ctx):
        # delete the message
        await ctx.message.delete()
        # stop execution
        await ctx.send(':gear: Restarting...')
        python = sys.executable
        os.execl(python, python, *sys.argv)
        await ctx.send(':white_check_mark: Restarted <@!742388119516741642>')
        sys.exit('bot has been restarted by bot owner')

def setup(bot):
    bot.add_cog(stop(bot))