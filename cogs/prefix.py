from discord.ext import commands
import json
from main import prefixes
import sys
import os

class prefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="prefix")
    @commands.has_permissions(manage_guild=True)
    async def _prefix(self, ctx, *, body=None):
        if body is None:
          with open("prefixes.json", "r") as f:
            json.load(f)
          try:
            prefix = prefixes[f'{ctx.guild.id}']
          except KeyError:
            prefix = "hh!"
          return await ctx.send(f"The prefix for this quild is: `{prefix}`")
        elif body == "reset":
          prefixes[f'{ctx.message.guild.id}'] = "hh!"
          with open("prefixes.json", "w") as f:
              json.dump(prefixes, f, indent=4)
          await ctx.send(f":white_check_mark: Reset this quild's prefix")
          python = sys.executable
          os.execl(python, python, *sys.argv)
          sys.exit('prefix reset: restarting client now')   
        else:
          if body.endswith("-"):
              prefixes[f'{ctx.message.guild.id}'] = body.replace("-", " ")
          else:
              prefixes[f'{ctx.message.guild.id}'] = body
          with open("prefixes.json", "w") as f:
              json.dump(prefixes, f, indent=4)
          await ctx.send(f":white_check_mark: Set prefix for this quild as: `{body.replace('-', ' ')}`")
          python = sys.executable
          os.execl(python, python, *sys.argv)
          sys.exit('prefix changed: restarting client now')



def setup(client):
    client.add_cog(prefix(client))