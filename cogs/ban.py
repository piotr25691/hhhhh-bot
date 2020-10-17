import discord
import re
from discord.ext import commands

owner = "603635602809946113"

class ban(commands.Cog):
     # ban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ban(self, ctx, *args):
        userid = re.sub('[^0-9]', '', args[0])
        print(userid)
        if "@everyone" in ctx.message.content:
            embedVar = discord.Embed(title=":x: Forbidden", description="You can't ban @everyone!", color=0xff0000)
            return await ctx.send(embed=embedVar)
        elif "@here" in ctx.message.content:
            embedVar = discord.Embed(title=":x: Forbidden", description="You can't ban @here!", color=0xff0000)
            return await ctx.send(embed=embedVar)
        elif not userid == owner:
            if userid == "":
                embedVar = discord.Embed(title=":x: Error", description="You need someone to ban.", color=0xff0000)
            await ctx.send(f":white_check_mark: Banned <@!{userid}>")
            return await ctx.guild.ban(discord.Object(id=userid))
        else:
            embedVar = discord.Embed(title=":x: Forbidden", description="You can't ban the owner of the bot!",
                                     color=0xff0000)
            return await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(ban(bot))