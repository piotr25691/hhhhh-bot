import discord
import math
from discord.ext import commands
from main import prefixes
from main import maintenance
from vars import *
from difflib import SequenceMatcher


class handler(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            try:
              global prefix
              prefix = prefixes[f'{message.guild.id}']
            except AttributeError:
              pass
        except KeyError:
            prefix = "hh!"

        if maintenance == False:
            try:
              if message.content in pings:
                e = discord.Embed(title=":information_source: Notice",
                                     description=f"Do you want my prefix? Just use `{prefix}`", color=0x7289da)
                e.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
                return await message.channel.send(embed=e)
            except UnboundLocalError:
              pass    
        else:
            pass
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        error = getattr(error, 'original', error)
        # client - nonexistent command
        if isinstance(error, commands.CommandNotFound):
            suggestion = None
            for command in client.all_commands:
                if client.all_commands[command].enabled and not client.all_commands[command].hidden:
                    ratio = round(SequenceMatcher(a=ctx.invoked_with, b=command).ratio(),
                                  1)
                    if ratio >= 0.7:
                        suggestion = command
                        break
            if suggestion is None:
              e = discord.Embed(colour=0xff0000, description=f"That command doesn't exist! Use `{prefix}help` for a list of commands.")
              e.set_author(name='Command not found', icon_url="https://i.imgur.com/OyDaCvd.png")
            else:
              e = discord.Embed(colour=0xff0000, description=f"That command doesn't exist! Did you perhaps mean `{prefix}{suggestion}`?")
              e.set_author(name='Command not found', icon_url="https://i.imgur.com/OyDaCvd.png")
                 
                 
            await ctx.send(embed=e)
        # client - command disabled
        elif isinstance(error, commands.DisabledCommand):
            e = discord.Embed(description="This command has been disabled.",
                                     color=0xff0000)
            e.set_author(name='Disabled', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=e, delete_after=10)
        # client - command on cooldown
        elif isinstance(error, commands.CommandOnCooldown):
            e = discord.Embed(
                                     description=f"You are ratelimited. Please try aqain in {math.ceil(error.retry_after)} seconds.",
                                     color=0xff0000)
            e.set_author(name='Ratelimited', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=e, delete_after=10)
        # user - missing permissions
        elif isinstance(error, commands.MissingPermissions):
            e = discord.Embed(description=f"You can't use this command.", color=0xff0000)
            e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=e, delete_after=10)
        # user - no DM
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                e = discord.Embed(description=f"You can't use this command in DMs.",
                                         color=0xff0000)
                e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                return await ctx.author.send(embed=e, delete_after=10)
            except discord.Forbidden:
                pass
                return
        # user - no permission
        elif isinstance(error, commands.CheckFailure):
            e = discord.Embed(description="You can't use this command.", color=0xff0000)
            e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=e, delete_after=10)
        elif isinstance(error, Exception):
          e = discord.Embed(title=":x: Command raised exception", description=f"```py\n{error} ```", color=0xff0000)
          e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
          return await ctx.send(embed=e)
        else:
          return  


def setup(client):
    client.add_cog(handler(client))