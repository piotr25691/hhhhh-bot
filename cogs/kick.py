import discord
import re
from discord.ext import commands

owner = "603635602809946113"

class kick(commands.Cog):
     # kick command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, *args):
        userid = re.sub('[^0-9]', '', args[0])
        if "@everyone" in ctx.message.content:
            embedVar = discord.Embed(title=":x: Forbidden", description="You can't kick @everyone!", color=0xff0000)
            return await ctx.send(embed=embedVar)
        elif "@here" in ctx.message.content:
            embedVar = discord.Embed(title=":x: Forbidden", description="You can't kick @here!", color=0xff0000)
            return await ctx.send(embed=embedVar)
        elif not userid == owner:
            try:
                user = ctx.guild.get_member(userid)
            except Exception as e:
                embedVar = discord.Embed(title=":x: Error", description="You need someone to kick.", color=0xff0000)
                return await ctx.send(embed=embedVar)
            await ctx.send(f":white_check_mark: Kicked <@!{userid}>")
            return await ctx.guild.kick(discord.Object(id=userid))
        else:
            embedVar = discord.Embed(title=":x: Forbidden", description="You can't kick the owner of the bot!",
                                     color=0xff0000)
            return await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(kick(bot))