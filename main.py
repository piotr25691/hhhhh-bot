# import required libraries

# discord api
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.tasks import loop

# async functions & sleep
import asyncio

# regex (g-detector)
import re

# eval
import inspect
import io
import textwrap
import traceback
from contextlib import redirect_stdout

# config
import json

# nitro command
import random
# 24/7
from webserver import keep_alive
# math command
import math
# datestamp
import datetime
import itertools
import os


bot = commands.Bot(command_prefix='hh!')
bot.remove_command('help')
bot.load_extension("cogs.say")
bot.load_extension("cogs.thewar")
bot.load_extension("cogs.help")
bot.load_extension("cogs.info")
bot.load_extension("cogs.uptime")
bot.load_extension("cogs.version")
bot.load_extension("cogs.changelog")
bot.load_extension("cogs.invite")
bot.load_extension("cogs.h")
bot.load_extension("cogs.safeeveryone")
bot.load_extension("cogs.ping")
bot.load_extension("cogs.purge")
bot.load_extension("cogs.math")
bot.load_extension("cogs.react")
bot.load_extension("cogs.msgcount")
bot.load_extension("cogs.dm")
bot.load_extension("cogs.avatar")
bot.load_extension("cogs.ban")
bot.load_extension("cogs.kick")
bot.load_extension("cogs.unban")
bot.load_extension("cogs.warn")
bot.load_extension("cogs.eval")
bot.load_extension("cogs.stop")
bot.load_extension("cogs.fix")
bot.load_extension("cogs.snipe")
bot.load_extension("cogs.editsnipe")

owner = "603635602809946113"
version = "1.1a"
build = "20200925"
totalcommands = "26"
global msg_
msg_ = None
startTime = datetime.datetime.utcnow()
clear = lambda: os.system('clear')

with open("removed.txt") as f:
    removed = int(f.read().strip())

# g delete count incrementer function


def increment_g():
    # define global variable
    global removed
    # increment the variable
    removed += 1
    # write the new value into a file
    with open("removed.txt", "w") as f:
        f.write(str(removed))
        f.close()

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

class hhhhh(commands.Cog):

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
            return
         pingresult = re.compile('<@!742388119516741642>', re.IGNORECASE).findall(msg)
         mobilepingresult = re.compile('<@742388119516741642>', re.IGNORECASE).findall(msg)
         # if any of the regexes match do the following
         if pingresult or mobilepingresult:
             embedVar = discord.Embed(title=":information_source: Notice", description="Do you want my prefix? Just use `hh!`", color=0x7289da)
             embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
             return await message.channel.send(embed=embedVar)
        # allow the bot to process commands
        
         await bot.process_commands(message)


@bot.event
async def on_ready():
    change_presence.start()
    bot.add_cog(hhhhh(bot))
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