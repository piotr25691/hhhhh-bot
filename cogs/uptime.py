import discord
import datetime
from discord.ext import commands
import time_utils

startTime = datetime.datetime.utcnow()

class uptime(commands.Cog):
    @commands.command(name='uptime', aliases=['upt'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def uptime_(self, ctx):
        sys_stamp = time_utils.get_sys_uptime()
        uptime_stamp = time_utils.get_bot_uptime(startTime)
        e = discord.Embed(title=":clock3: Uptime", description=f"Bot: {uptime_stamp}**\n**System: {sys_stamp}",
                                 color=0x7289da)
        e.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
        return await ctx.send(embed=e)

def setup(client):
    client.add_cog(uptime(client))