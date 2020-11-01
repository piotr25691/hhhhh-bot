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
maintenance = False
import math
import secrets
import re

with open("prefixes.json") as f:
    prefixes = json.load(f)
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

    @commands.Cog.listener()
    async def on_message(message):

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

        if "gatos" in message.content:
            await message.channel.purge(limit=5)

        # if any of the regexes match do the following
        if maintenance == False:
            if message.content in pings:
                embedVar = discord.Embed(title=":information_source: Notice",
                                     description=f"Do you want my prefix? Just use `{prefix}`", color=0x7289da)
                embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
                return await message.channel.send(embed=embedVar)
        else:
            pass
        # allow the bot to process commands
        
        if "@someone" in message.content:
            member = random.choice(bot.users)
            while member.bot is True:
                member = random.choice(bot.users)
                if member.bot is False:
                    break
        
            await message.channel.send(f"@someone ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||| |||| || <@!{member.id}>")

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
