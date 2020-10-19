import discord
import re
from discord.ext import commands
from discord.ext.commands import Bot
tos = ["nigga", "nigger", "nigguh"]

class dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    # changelog command
    # dm command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dm(self, ctx, *, body):
        userid = re.sub('[^0-9]','', body[:22])
        user = await self.bot.fetch_user(userid)
        for word in tos:
            if word in ctx.message.content:
                return await ctx.send("Absolutely not!\nAre you trying to get me banned?")
            else:
                return await user.send(body[22:])


def setup(bot):
    bot.add_cog(dm(bot))