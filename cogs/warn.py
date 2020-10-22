import discord
import re
from discord.ext import commands
from discord.ext.commands import bot
from vars import *
   
class warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def warn(self, ctx, *, body):
        userid = re.sub('[^0-9]', '', body[:22])
        user = await self.bot.fetch_user(userid)
        reason = body[22:]
        reasoncheck = f"h{reason}"
        if userid == owner:
            embedVar = discord.Embed(description="You can't warn the owner of the bot!",
                                     color=0xff0000)
            embedVar.set_author(name='Forbidden', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar)
        elif userid == "742388119516741642":
            embedVar = discord.Embed(description="You can't warn me!", color=0xff0000)
            embedVar.set_author(name='Forbidden', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar)
        else:
            if not reasoncheck == "h":
                await ctx.send(f":white_check_mark: <@!{userid}> has been warned because:{reason}")
                await user.send(f"You have been warned in {ctx.guild.name} for:{reason}")
            else:
                await ctx.send(f":white_check_mark: <@!{userid}> has been warned.")
                await user.send(f"You have been warned in {ctx.guild.name}.")


def setup(bot):
    bot.add_cog(warn(bot))