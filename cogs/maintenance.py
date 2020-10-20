import discord
from discord.ext import commands


class maintenance(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        error = getattr(error, 'original', error)
        if isinstance(error, commands.CommandNotFound):
            embedVar = discord.Embed(title=":x: Maintenance Mode", description="The bot is in maintenance mode.\nYou can't use any commands riqht now.",
                                     color=0xff0000)
            return await ctx.send(embed=embedVar, delete_after=10)

def setup(bot):
    bot.add_cog(maintenance(bot))