import discord
import datetime
from discord.ext import commands
from vars import *
from main import prefixes

startTime = datetime.datetime.utcnow()

class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    # info command
    @commands.command(name='info')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def info_(self, ctx):
        try:
            prefix = prefixes[f'{ctx.guild.id}']
        except KeyError:
            prefix = "hh!"
        dev = await self.client.fetch_user(603635602809946113)
        ping = f"{round(self.client.latency * 1000, 1)}ms"
        e = discord.Embed(
                                 description=f"Seems like you want to qet some info about me!\nSee this.\nFor help use `{prefix}help`.",
                                 color=0x7289da)
        e.set_author(name='Information', icon_url="https://i.imgur.com/A8g1ViW.png")
        e.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
        e.add_field(name="<:4228_discord_client_dev:727548651001348196> Developer", value=f"{dev}", inline=True)
        e.add_field(name=":regional_indicator_v: Current version", value=f"{version} \n(Build {build})",
                           inline=True)
        e.add_field(name=":information_source: Details",
                           value=f"\🏘️ Server count: {len(self.client.guilds)}\n\🏓 Pinq: {ping}\n\⚙️ Commands: {totalcommands}\n\🧑‍🤝‍🧑 Total members: {len(self.client.users)}")                 
        return await ctx.send(embed=e)

def setup(client):
    client.add_cog(info(client))