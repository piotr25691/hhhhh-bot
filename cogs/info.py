import discord
import datetime
from discord.ext import commands
from discord.ext.commands import Bot

startTime = datetime.datetime.utcnow()
owner = "603635602809946113"
version = "1.1a"
build = "20200925"
totalcommands = "26"

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # info command
    @commands.command(name='info')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def info_(self, ctx):
        dev = await self.bot.fetch_user(603635602809946113)
        ping = f"{round(self.bot.latency * 1000, 1)}ms"
        now = datetime.datetime.utcnow()  # Timestamp of when uptime function is run
        delta = now - startTime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days:
            time_format = "`{d}` days, `{h}` hours, `{m}` minutes, and `{s}` seconds."
        else:
            time_format = "`{h}` hours, `{m}` minutes, and `{s}` seconds."
        uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
        embedVar = discord.Embed(title="Information",
                                 description="Seems like you want to qet some info about me!\nSee this.\nFor help use `hh!help`.",
                                 color=0x7289da)
        embedVar.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
        embedVar.add_field(name="<:4228_discord_bot_dev:727548651001348196> Developer", value=f"{dev}", inline=True)
        embedVar.add_field(name=":regional_indicator_v: Current version", value=f"{version} \n(Build {build})",
                           inline=True)
        embedVar.add_field(name=":information_source: Details",
                           value=f":homes: Server count: {len(self.bot.guilds)}\n:ping_pong: Pinq: {ping}\n:gear: Commands: {totalcommands}\n:alarm_clock: Uptime: {uptime_stamp}\n:people_holding_hands: Total members: {len(self.bot.users)}")
        return await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(info(bot))