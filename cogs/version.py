import discord
import datetime
from discord.ext import commands
from discord.ext.commands import Bot
from vars import *

class version(commands.Cog):
    # version command
    @commands.command(name='version')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def version_(self, ctx):
        embedVar = discord.Embed(color=0x7289da)
        embedVar.set_author(name='Version Information', icon_url="https://i.imgur.com/A8g1ViW.png")
        embedVar.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
        embedVar.add_field(name="Current version", value=f"{version_}", inline=True)
        embedVar.add_field(name="Current build", value=f"Build {build}", inline=True)
        return await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(version(bot))