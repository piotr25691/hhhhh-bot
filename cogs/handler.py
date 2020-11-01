import discord
import math
from discord.ext import commands
from main import prefixes
from main import maintenance
from vars import *


class handler(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            prefix = prefixes[f'{message.guild.id}']
        except KeyError:
            prefix = "hh!"

        if maintenance == False:
            if message.content in pings:
                embedVar = discord.Embed(title=":information_source: Notice",
                                     description=f"Do you want my prefix? Just use `{prefix}`", color=0x7289da)
                embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
                return await message.channel.send(embed=embedVar)
        else:
            pass
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        error = getattr(error, 'original', error)
        # bot - nonexistent command
        # bot - nonexistent command
        if isinstance(error, commands.CommandNotFound):
            await ctx.message.delete()
            embedVar = discord.Embed(description="This command does not exist.",
                                         color=0xff0000)
            embedVar.set_author(name='Command Not Found', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar, delete_after=10)
        # bot - command disabled
        if isinstance(error, commands.DisabledCommand):
            userid = ctx.message.author.id
            embedVar = discord.Embed(description="This command has been disabled.",
                                     color=0xff0000)
            embedVar.set_author(name='Disabled', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar, delete_after=10)
        # bot - command on cooldown
        if isinstance(error, commands.CommandOnCooldown):
            embedVar = discord.Embed(
                                     description=f"You are ratelimited. Please try aqain in {math.ceil(error.retry_after)} seconds.",
                                     color=0xff0000)
            embedVar.set_author(name='Ratelimited', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar, delete_after=10)
        # user - missing permissions
        if isinstance(error, commands.MissingPermissions):
            embedVar = discord.Embed(description=f"You can't use this command.", color=0xff0000)
            embedVar.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar, delete_after=10)
        # user - no DM
        if isinstance(error, commands.NoPrivateMessage):
            userid = ctx.message.author.id
            try:
                embedVar = discord.Embed(description=f"You can't use this command in DMs.",
                                         color=0xff0000)
                embedVar.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                return await ctx.author.send(embed=embedVar, delete_after=10)
            except discord.Forbidden:
                pass
                return
        # user - no permission
        if isinstance(error, commands.CheckFailure):
            embedVar = discord.Embed(description=f"You can't use this command.", color=0xff0000)
            embedVar.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar, delete_after=10)
        


def setup(bot):
    bot.add_cog(handler(bot))
