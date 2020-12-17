
import discord
import datetime
from discord.ext import commands
from discord.ext.tasks import loop
from difflib import SequenceMatcher
from AntiSpam import AntiSpamHandler
import asyncio
import json
import random
from webserver import keep_alive
from vars import *

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

ok = 0
spam = 0
messages = 0
maintenance = False
default_prefix = "hh!"

def prefix(client, message):
    try:
      id = message.guild.id
    except AttributeError:
      pass
    try:
        return prefixes[f'{id}']
    except Exception:
        return default_prefix

intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents, owner_ids=[603635602809946113, 444550944110149633, 429935667737264139, 350325552344858624])
client.handler = AntiSpamHandler(client)
client.remove_command('help')
if maintenance == True:
    client.load_extension('cogs.maintenance')
    client.load_extension('cogs.restart')
else:
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
    client.unload_extension('cogs.maintenance')

@loop(seconds=1800)
async def change_presence():
    activity = discord.Activity(type=discord.ActivityType.streaming, name=f"h | Use hh!help | {version}",
                                    url="https://www.youtube.com/watch?v=DwjbP7aihxQ")
    await client.change_presence(status='dnd', activity=activity)
    await asyncio.sleep(600)
    activity = discord.Activity(type=discord.ActivityType.watching, name=f"out for g-spies | Use hh!help | {version}")
    await client.change_presence(status='dnd', activity=activity)
    await asyncio.sleep(600)
    activity = discord.Activity(type=discord.ActivityType.watching, name=f"h-posters | Use hh!help | {version}")
    await client.change_presence(status='dnd', activity=activity)
    await asyncio.sleep(600)

class maincog(commands.Cog):
    @client.event
    async def on_message(message):
        if message.guild is None:
          if not message.author.bot:
            return await message.channel.send("Commands in DMs don't work right now, so there's no need to talk to me here... :smile:") 
        try:
          if "h!g-spy" in message.content and "603635602809946113" in message.content:
            if message.author.id == 603635602809946113:
              return
            await message.channel.send("<:unoreverse:774916409519243324>")
            await message.channel.send(
              f":x: <@!{message.author.id}>, it is forbidden to give g-spy to Lunah!\nYou have received g-spy yourself :sunglasses:")
            role = discord.utils.get(message.guild.roles, name="g-spy")
            await message.author.add_roles(role, reason="Attempted to give g-spy to Lunah, which is forbidden")
            user = message.guild.get_member(603635602809946113)
            await user.remove_roles(role, reason="Precaution to keep the g-spy role removed of Lunah")

            user = message.guild.get_member(603635602809946113)
            role = discord.utils.get(message.guild.roles, name="g-spy")
            for x in user.roles:
              if x.name == "g-spy":
                await user.remove_roles(role, reason="Precaution to keep the g-spy role removed of Lunah")
                await message.channel.send(f"it is forbidden to add g-spy to {user.name}!\nplease don't do that")
                break

          if message.content == "ok" and not message.author.bot and not message.author.id == 603635602809946113:
            global ok
            ok = ok + 1
            if ok > 5:
                await message.channel.send(f"Whoa there, <@!{message.author.id}>, stop spamming OK!")
                ok = 0
            await message.add_reaction("<:shut:773514956472844298>")
            await message.add_reaction("🆙")
            await message.add_reaction("<:no:773258649496715294>")
            await message.add_reaction("1️⃣")
            await message.add_reaction("🇨")
            await message.add_reaction("🅰️")
            await message.add_reaction("🇷")
            await message.add_reaction("🇪")
            await message.add_reaction("🇸")
            await message.channel.send("shut up no one cares")
            ok = 0

          hresult = re.compile(r'\bh+\b', re.IGNORECASE).findall(message.content)

          try:
            if message.guild.id == 773249498104201228:
              if not message.author.bot:
                global messages
                messages = messages + 1
                messages_data[str(datetime.date.today()).replace("-", "")] = messages
                with open("message_metric.json", "w") as f:
                  json.dump(messages_data, f, indent=4)
          except AttributeError:
            pass

          try:
            prefix = prefixes[f'{message.guild.id}']
          except Exception as e:
            prefix = "hh!"

          msg = message.content
          if message.author.bot:
            if message.author.id == 759674875605680158:
              pass
            else:
              return

          if message.content.casefold() in map(str.casefold, forbidden):
            await message.delete()
            h = await message.channel.send("no")
            await asyncio.sleep(2)
            await h.delete()

          if hresult:
            if prefix in message.content:
              pass
            else:
              global hcount
              hcount = hcount + 1
              with open("hcount.txt", "w") as f:
                f.write(str(hcount))
                f.close()

          if message.content == "@someone":
            member = random.choice(message.guild.members)
            while member.bot is True:
              member = random.choice(message.guild.members)
              if member.bot is False:
                break

          await message.channel.send(f"<@!{member.id}>")
        except:
          pass
        if hresult:
          pass        
        elif message.author.guild_permissions.administrator is True:
          pass
        else:
          client.handler.propagate(message)
        await client.process_commands(message)


@client.event
async def on_ready():
    channel = client.get_channel(739229517242957976)
    htime = datetime.datetime.now()
    hcomp = datetime.timedelta(hours=1)
    e = discord.Embed(title='hhhhh started', description=f'Started on {str(htime+hcomp)[:16]} (CET)', color=discord.Colour.blurple())
    if maintenance == True:
        activity = discord.Game(name=f"Maintenance mode | {version}")
    else:
        change_presence.start()
        activity = discord.Activity(type=discord.ActivityType.streaming, name=f"h | Use hh!help | {version}",
                                url="https://www.youtube.com/watch?v=DwjbP7aihxQ")
    await client.change_presence(status='dnd', activity=activity)
    if maintenance == True:
        print("Bot is ready (maintenance)")
        print("Owner ID: " + owner)
        await channel.send(embed=e)
    else:
        print("Bot is ready")
        print("Owner ID: " + owner)
        await channel.send(embed=e)


def main():
    keep_alive()
    with open("config.json") as fh:
        client.config = json.load(fh)
        client.run(client.config['token'])


if __name__ == "__main__":
    main()