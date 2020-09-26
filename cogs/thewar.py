import discord
from discord.ext import commands

class thewar(commands.Cog):
    # the war
    @commands.command(aliases=['the'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def thewar(self, ctx):
        msg = ctx.message.content
        if "the war" in msg:
            return await ctx.send("the war")
        else:
            return await ctx.send("war")

def setup(bot):
    bot.add_cog(thewar(bot))