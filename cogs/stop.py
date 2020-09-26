import discord
from discord.ext import commands
from discord.ext.commands import Bot


class stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # stop command
    @commands.command(aliases=['kill', 'die'])
    # check whether the bot owner tries to kill the bot from chat or not
    @commands.is_owner()
    async def terminate(self, ctx):
        # delete the message
        await ctx.message.delete()
        # stop execution
        return await self.bot.logout()

def setup(bot):
    bot.add_cog(stop(bot))