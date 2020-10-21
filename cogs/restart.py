import discord
from discord.ext import commands
from discord.ext.commands import Bot
import sys
import os
import asyncio


class stop(commands.Cog):
    # stop command
    @commands.command(aliases=['restart', 'reboot'])
    @commands.is_owner()
    async def restart_(self, ctx):
        # delete the message
        await ctx.message.delete()
        # stop execution
        await ctx.send(':gear: Restarting...')
        await asyncio.sleep(5)
        await ctx.send(':white_check_mark: Restarted <@!742388119516741642>')
        python = sys.executable
        os.execl(python, python, *sys.argv)
        sys.exit('restarted bot')


def setup(bot):
    bot.add_cog(stop(bot))