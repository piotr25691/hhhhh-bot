import discord
from discord.ext import commands

class kick(commands.Cog):
     # kick command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, member:discord.Member=None, *, body=None):
        if member is None:
         return await ctx.send("Who are you kicking? :thinking:")
        if not member.id == 603635602809946113 and not member.id == 742388119516741642 and not member.top_role >= ctx.message.author.top_role:
          await ctx.guild.kick(member, reason=body)
          await ctx.send(f":white_check_mark: Successfully kicked {member}!\nReason: {body}")
        else:
          if member.id == 603635602809946113:
            return await ctx.send(f":x: You cannot kick {member}!")
          if member.id == 742388119516741642:
            return await ctx.send(":x: You cannot kick me!")
          if member.top_role >= ctx.message.author.top_role:
            return await ctx.send(f":x: You cannot kick {member} as that user has a higher role than you!")  


def setup(client):
    client.add_cog(kick(client))