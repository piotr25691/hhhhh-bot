import discord
from discord.ext import commands
import json
from main import prefixes
import sys
import os

class prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="prefix")
    @commands.has_permissions(manage_guild=True)
    async def _prefix(self, ctx, *, body):
        if body.endswith("-"):
            prefixes[f'{ctx.message.guild.id}'] = body.replace("-", " ")
        else:
            prefixes[f'{ctx.message.guild.id}'] = body
        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f)
        await ctx.send(f":white_check_mark: Set prefix for this guild as: `{body.replace('-', ' ')}`")
        python = sys.executable
        os.execl(python, python, *sys.argv)
        sys.exit('prefix changed: restarting bot now')



def setup(bot):
    bot.add_cog(prefix(bot))

