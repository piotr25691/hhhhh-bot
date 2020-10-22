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
            embedVar = discord.Embed(description="You can't kick @everyone!", color=0xff0000)
            embedVar.set_author(name='Forbidden', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar)
        elif "@here" in ctx.message.content:
            embedVar = discord.Embed(description="You can't kick @here!", color=0xff0000)
            embedVar.set_author(name='Forbidden', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar)
        elif userid == "742388119516741642":
            embedVar = discord.Embed(description="You can't kick me!", color=0xff0000)
            embedVar.set_author(name='Forbidden', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar)
        elif userid == "610640581911248926":
            embedVar = discord.Embed(description="You can't kick <@!610640581911248926>!",
                                     color=0xff0000)
            embedVar.set_author(name='Forbidden', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar)
        elif not userid == owner:
            if userid == "":
                embedVar = discord.Embed(description="You need someone to kick.", color=0xff0000)
                embedVar.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                return await ctx.send(embed=embedVar)
            await ctx.send(f":white_check_mark: Banned <@!{userid}>")
            return await ctx.guild.ban(discord.Object(id=userid))
        else:
            embedVar = discord.Embed(description="You can't kick the owner of the bot!",
                                     color=0xff0000)
            embedVar.set_author(name='Forbidden', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(kick(bot))