import discord
from discord.ext import commands

class hcount(commands.Cog):
    @commands.command(name="hcount")
    async def hcount(self, ctx):
        with open("hcount.txt") as f:
            hcount = int(f.read().strip())
        embedVar = discord.Embed(title="<:ddr_h:719126723987505183> H Count", description=f"There have been {hcount} H's sent in total.",
                                 color=0x7289da)
        await ctx.send(embed=embedVar)
def setup(bot):
    bot.add_cog(hcount(bot))
