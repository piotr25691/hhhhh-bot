import discord
from discord.ext import commands
from vars import *
import sys
import os
from main import client
import psutil
from hurry.filesize import size
import platform

class sudo(commands.Cog):
    def __init__(self, bot):
        self.client = client
    
    @commands.command(hidden=True)
    @commands.is_owner()
    async def sudo(self, ctx, *, body=None):
      if not body is None:
        if body == "help":
          e = discord.Embed(title="<:4228_discord_bot_dev:727548651001348196> Sudo Help", description="These are the sudo commands :flushed:", color=0x7289da)
          e.add_field(name="\u200b", value="fix prefix\n```Fixes the prefix incase it broke```\nreload bot\n```Reboots the bot```\nstop bot\n```Stops the bot```\nshow systeminfo\n```Shows info about the hostinq system```")
          await ctx.send(embed=e)
          return await ctx.message.add_reaction("👌")
        elif body == "h":
          await ctx.send("h")
        elif body.startswith("raise"):
          try:
            errortype = body.split(None, 2)[1]
            content = body.split(None, 2)[2]
            print(errortype)
            print(content)
          except IndexError:
            return await ctx.send("lol what are you gonna do with this error")
          if errortype == "syntax":
            if content is None:
              raise TypeError("no error description was specified")
            else:
              raise SyntaxError(content)
          elif errortype == "indent":
            if content is None:
              raise TypeError("no error description was specified")
            else:
              raise IndentationError(content)
          elif errortype == "type":
            if content is None:
              raise TypeError("no error description was specified")
            else:
              raise TypeError(content)
          elif errortype == "value":
            if content is None:
              raise TypeError("no error description was specified")
            else:
              raise ValueError(content)
          elif errortype == "attribute":
            if content is None:
              raise TypeError("no error description was specified")
            else:
              raise AttributeError(content)
          else:
            raise NameError("not a valid error type")
        elif body.startswith("find"):
          to_find = body[5:]
          if to_find == "":
            await ctx.message.add_reaction("❌")
            return await ctx.send("what are you looking for dum")
          channel = ctx.guild.get_channel(ctx.channel.id)
          await ctx.send(f"Looking around for {to_find}...\nPlease wait.")
          with ctx.channel.typing():
            channel = channel or ctx.channel
            count = 0
            async for message in channel.history(limit=None):
                if message.content == to_find:
                  count += 1
          await ctx.send(f"I found {count} {to_find} in <#{channel.id}>")
        elif body == "fix prefix":  
          activity = discord.Activity(type=discord.ActivityType.streaming, name=f"h | Use hh!help | {version}",
                                    url="https://www.youtube.com/watch?v=DwjbP7aihxQ")
          await self.client.change_presence(status='dnd', activity=activity)
          return await ctx.message.add_reaction("👌")
        elif body == "fix":
          await ctx.send("lol what do you want to fix")
          return await ctx.message.add_reaction("❔")
        elif body == "reload bot":
          # stop execution
          await ctx.message.add_reaction("👌")
          python = sys.executable
          os.execl(python, python, *sys.argv)
          sys.exit('restarted bot')
        elif body == "reload":
          await ctx.send("lol what do you want to reload")
          return await ctx.message.add_reaction("❔")
        elif body == "stop bot":
          # stop execution
          await ctx.message.add_reaction("👌")
          sys.exit('bot has been stopped by bot owner')
        elif body == "stop":
          await ctx.send("lol what do you want to stop")
          return await ctx.message.add_reaction("❔")  
        elif body == "show systeminfo":
          await ctx.message.add_reaction("👌")
          e = discord.Embed(
                    title="Host System Information",
                    color=0x7289da
                )

          e.add_field(name="‎", value="**CPU**", inline=False)
          e.add_field(name="CPU Usaqe", value=str(psutil.cpu_percent()) + "%")
          e.add_field(name="Loqical CPU Count", value=psutil.cpu_count())

          mem = psutil.virtual_memory()
          e.add_field(name="‎", value="**Memory**", inline=False)
          e.add_field(name="Total Memory", value=size(mem.total) + "B")
          e.add_field(name="Available Memory", value=size(mem.available) + "B")
          e.add_field(name="Memory Usaqe", value=str(mem.percent) + "%")

          disk = psutil.disk_usage("/")
          e.add_field(name="‎", value="**Disk**", inline=False)
          e.add_field(name="Total Space", value=size(disk.total) + "B")
          e.add_field(name="Used Space", value=size(disk.used) + "B")
          e.add_field(name="Free Space", value=size(disk.free) + "B")
          e.add_field(name="Disk Usaqe", value=str(disk.percent) + "%")

          net = psutil.net_io_counters()
          e.add_field(name="‎", value="**Network**", inline=False)
          e.add_field(name="Packets Sent", value=net.packets_sent)
          e.add_field(name="Packets Received", value=net.packets_recv)
          e.add_field(name="Bytes Sent", value=size(net.bytes_sent) + "B")
          e.add_field(name="Bytes Received", value=size(net.bytes_recv) + "B")

          e.add_field(name="‎", value="**OS**", inline=False)
          e.add_field(name="System", value=platform.system())
          if len(platform.release()) != 0:
            e.add_field(name="Release", value=platform.release())
          else:
            e.add_field(name="Release", value="???")
          if len(platform.version()) != 0:
            e.add_field(name="Version", value=platform.version())
          else:
            e.add_field(name="Release", value="???")
            
          await ctx.send(embed=e)
        elif body == "show":
            await ctx.send("lol what do you want to show")
            return await ctx.message.add_reaction("❔") 
        else:
          await ctx.send("lol thats not a valid action")
          return await ctx.message.add_reaction("❌")   
      else:
        await ctx.send("lol what do you want to do") 
        return await ctx.message.add_reaction("❔")                  
        
        
def setup(bot):
    bot.add_cog(sudo(bot))