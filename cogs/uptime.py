import discord
import datetime
from discord.ext import commands
from discord.ext.commands import Bot

startTime = datetime.datetime.utcnow()

class uptime(commands.Cog):
    @commands.command(name='uptime', aliases=['upt'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def uptime_(self, ctx):
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
        embedVar = discord.Embed(title=":alarm_clock: Uptime", description=f"**I've been runninq for {uptime_stamp}**",
                                 color=0x7289da)
        embedVar.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
        return await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(uptime(bot))