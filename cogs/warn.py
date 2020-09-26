import discord
import re
from discord.ext import commands
from discord.ext.commands import bot
owner = "603635602809946113"
   
class warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def warn(self, ctx, *args):
        userid = re.sub('[^0-9]', '', args[0])
        reason = re.sub(f'hh!warn <@!{userid}>', '', ctx.message.content)
        mobilereason = re.sub(f'hh!warn <@{userid}> --mobile', '', ctx.message.content)
        reasoncheck = f"h{reason}"
        mobilereasoncheck = f"h{mobilereason}"
        user = await self.bot.fetch_user(userid)
        if userid == owner:
            embedVar = discord.Embed(title=":x: Forbidden", description="You can't warn the owner of the bot!",
                                     color=0xff0000)
            return await ctx.send(embed=embedVar)
        elif userid == "742388119516741642":
            embedVar = discord.Embed(title=":x: Forbidden", description="You can't warn me!", color=0xff0000)
            return await ctx.send(embed=embedVar)
        else:
            if not "--mobile" in ctx.message.content:
                if not reasoncheck == "h":
                    await ctx.send(f":white_check_mark: <@!{userid}> has been warned because:{reason}")
                    await user.send(f"You have been warned in {ctx.guild.name} for:{reason}")
                else:
                    await ctx.send(f":white_check_mark: <@!{userid}> has been warned.")
                    await user.send(f"You have been warned in {ctx.guild.name}.")
            else:
                if not mobilereasoncheck == "h":
                    await ctx.send(f":white_check_mark: <@!{userid}> has been warned because:{mobilereason}")
                    await user.send(f"You have been warned in {ctx.guild.name} for:{mobilereason}")
                else:
                    await ctx.send(f":white_check_mark: <@!{userid}> has been warned.")
                    await user.send(f"You have been warned in {ctx.guild.name}.")


def setup(bot):
    bot.add_cog(warn(bot))