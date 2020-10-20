# import required libraries

# discord api
import discord
from discord.ext import commands
from discord.ext.tasks import loop

# async functions & sleep
import asyncio

# config and prefix
import json

# 24/7
from webserver import keep_alive

# variables
from vars import *

import math
import secrets
import re

with open("prefixes.json") as f:
    prefixes = json.load(f)
default_prefix = "hh!"


def prefix(bot, message):
    id = message.guild.id
    try:
        prefix = prefixes[f'{id}']
        global prefix_
        prefix_ = prefixes[f'{id}']
        return prefix
    except KeyError:
        return default_prefix


bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@loop(seconds=1800)
async def change_presence():
    activity = discord.Activity(type=discord.ActivityType.streaming, name=f"h | Use hh!help | {version}",
                                    url="https://www.youtube.com/watch?v=DwjbP7aihxQ")
    await bot.change_presence(status='dnd', activity=activity)
    await asyncio.sleep(600)
    activity = discord.Activity(type=discord.ActivityType.watching, name=f"out for g-spies | Use hh!help | {version}")
    await bot.change_presence(status='dnd', activity=activity)
    await asyncio.sleep(600)
    activity = discord.Activity(type=discord.ActivityType.watching, name=f"out for h | Use hh!help | {version}")
    await bot.change_presence(status='dnd', activity=activity)
    await asyncio.sleep(600)

class maincog(commands.Cog):

    # initialize bot status and print bot is ready
    # error handler
    @bot.event
    async def on_command_error(ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        error = getattr(error, 'original', error)
        # bot - nonexistent command
        if isinstance(error, commands.CommandNotFound):
            await ctx.message.delete()
            embedVar = discord.Embed(title=":x: Command Not Found", description="This command does not exist.",
                                     color=0xff0000)
            return await ctx.send(embed=embedVar, delete_after=10)
        # bot - command disabled
        if isinstance(error, commands.DisabledCommand):
            userid = ctx.message.author.id
            embedVar = discord.Embed(title=":x: Disabled", description="This command has been disabled.",
                                     color=0xff0000)
            return await ctx.send(embed=embedVar, delete_after=10)
        # bot - command on cooldown
        if isinstance(error, commands.CommandOnCooldown):
            embedVar = discord.Embed(title=":x: Ratelimited",
                                     description=f"You are ratelimited. Please try aqain in {math.ceil(error.retry_after)} seconds.",
                                     color=0xff0000)
            return await ctx.send(embed=embedVar, delete_after=10)
        # user - missing permissions
        if isinstance(error, commands.MissingPermissions):
            embedVar = discord.Embed(title=":x: Error", description=f"You can't use this command.", color=0xff0000)
            return await ctx.send(embed=embedVar, delete_after=10)
        # user - no DM
        if isinstance(error, commands.NoPrivateMessage):
            userid = ctx.message.author.id
            try:
                embedVar = discord.Embed(title=":x: Error", description=f"You can't use this command in DMs.",
                                         color=0xff0000)
                return await ctx.author.send(embed=embedVar, delete_after=10)
            except discord.Forbidden:
                pass
                return
        # user - no permission
        if isinstance(error, commands.CheckFailure):
            embedVar = discord.Embed(title=":x: Error", description=f"You can't use this command.", color=0xff0000)
            return await ctx.send(embed=embedVar, delete_after=10)

    # g detector (recoded) (logs g rather than remove)

    @bot.event
    async def on_message(message):

        msg = message.content
        if message.author.bot:
            if message.author.id == 759674875605680158:
                pass
            else:
                return

        if "```http" in message.content:
            if message.channel.id == 759680439778148405:
                return await message.channel.send(
                    f":gear: Keep-Online:tm: packet registered\nPacket ID: {secrets.token_hex(16)}")
            else:
                pass

        if message.content.casefold() in map(str.casefold, forbidden):
            await message.delete()
            h = await message.channel.send("no")
            await asyncio.sleep(2)
            await h.delete()

        hresult = re.compile(r'\bh+\b', re.IGNORECASE).findall(message.content)

        if hresult:
            if prefix_ in message.content:
                pass
            else:
                global hcount
                hcount = hcount + 1
                with open("hcount.txt", "w") as f:
                    f.write(str(hcount))
                    f.close()

        if "gatos" in message.content:
            await message.channel.purge(limit=5)

        # if any of the regexes match do the following
        if message.content in pings:
            embedVar = discord.Embed(title=":information_source: Notice",
                                     description=f"Do you want my prefix? Just use `{prefix_}`", color=0x7289da)
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            return await message.channel.send(embed=embedVar)
        # allow the bot to process commands

        await bot.process_commands(message)


@bot.event
async def on_ready():
    change_presence.start()
    activity = discord.Activity(type=discord.ActivityType.streaming, name=f"h | Use hh!help | {version}",
                                url="https://www.youtube.com/watch?v=DwjbP7aihxQ")
    await bot.change_presence(status='dnd', activity=activity)
    print("Bot is ready")
    print("Owner ID: " + owner)


def main():
    keep_alive()
    with open('config.json') as fh:
        bot.config = json.load(fh)
        bot.run(bot.config['token'])


if __name__ == "__main__":
    main()
