import discord
import re
from discord.ext import commands

class unban(commands.Cog):
     # unban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unban(self, ctx, *args):
        userid = re.sub('[^0-9]', '', args[0])
        await ctx.send(f":white_check_mark: Unbanned <@!{userid}>")
        return await ctx.guild.unban(discord.Object(id=userid))


def setup(bot):
    bot.add_cog(unban(bot))