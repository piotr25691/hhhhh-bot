# import required libraries

# discord api
import discord
from discord.ext import commands
from discord.ext.tasks import loop

# async functions & sleep
import asyncio

# config and prefix
import json
import math

# 24/7

# variables
from vars import *
messages = 0
maintenance = False
hbot_mode = True
import secrets
import re

with open("prefixes.json") as f:
	prefixes = json.load(f)
with open("message_metric.json") as f:
    messages_data = json.load(f)
try:
    messages = int(messages_data[str(datetime.date.today()).replace("-", "")])
except KeyError:
    messages = 0

default_prefix = "hh!"

def prefix(bot, message):
    id = message.guild.id
    try:
        return prefixes[f'{id}']
    except KeyError:
        return default_prefix


bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command('help')
if maintenance == True:
    bot.load_extension('cogs.maintenance')
    bot.load_extension('cogs.restart')
else:
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
    bot.unload_extension('cogs.maintenance')

@loop(seconds=1800)
async def change_presence():
    activity = discord.Activity(type=discord.ActivityType.streaming, name=f"h | Use hh!help | {version}",
                                    url="https://www.youtube.com/watch?v=DwjbP7aihxQ")
    await bot.change_presence(status='dnd', activity=activity)
    await asyncio.sleep(600)
    activity = discord.Activity(type=discord.ActivityType.watching, name=f"out for g-spies | Use hh!help | {version}")
    await bot.change_presence(status='dnd', activity=activity)
    await asyncio.sleep(600)
    activity = discord.Activity(type=discord.ActivityType.watching, name=f"h-posters | Use hh!help | {version}")
    await bot.change_presence(status='dnd', activity=activity)
    await asyncio.sleep(600)

class maincog(commands.Cog):
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

    @bot.event
    async def on_message(message):
        if message.guild.id == 773249498104201228:
            if not message.author.bot:
                global messages
                messages = messages+1
                messages_data[str(datetime.date.today()).replace("-", "")] = messages
                with open("message_metric.json", "w") as f:
                    json.dump(messages_data, f)

        try:
            prefix = prefixes[f'{message.guild.id}']
        except KeyError:
            prefix = "hh!"

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
            if prefix in message.content:
                pass
            else:
                global hcount
                hcount = hcount + 1
                with open("hcount.txt", "w") as f:
                    f.write(str(hcount))
                    f.close()

        await bot.process_commands(message)


@bot.event
async def on_ready():
    if maintenance == True:
        activity = discord.Game(name=f"Maintenance mode | {version}")
    else:
        change_presence.start()
        activity = discord.Activity(type=discord.ActivityType.streaming, name=f"h | Use hh!help | {version}",
                                url="https://www.youtube.com/watch?v=DwjbP7aihxQ")
    await bot.change_presence(status='dnd', activity=activity)
    if maintenance == True:
        print("Bot is ready (maintenance)")
        print("Owner ID: " + owner)
    else:
        print("Bot is ready")
        print("Owner ID: " + owner)


def main():
    keep_alive()
    with open("config.json") as fh:
        bot.config = json.load(fh)
        bot.run(bot.config['token'])


if __name__ == "__main__":
    main()
