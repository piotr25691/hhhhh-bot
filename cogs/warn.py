import discord
import re
from discord.ext import commands
from vars import *
   
class warn(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def warn(self, ctx, member:discord.Member=None, *, reason=None):
        if member is None:
          return await ctx.send("Who are you warning? :thinking:")
        if not member.id == 603635602809946113 and not member.id == 742388119516741642:
          if reason is not None:
            try:
                await member.send(f"You have been warned in {ctx.guild.name} for:{reason}")
            except discord.HTTPException:
                await ctx.send(f":white_check_mark: {member} has been warned because: {reason}, I couldn't DM them.")
            else:
                await ctx.send(f":white_check_mark: {member} has been warned because: {reason}")
          else:          
            try:
              await member.send(f"You have been warned in {ctx.guild.name}.")
            except discord.HTTPException:
              await ctx.send(f":white_check_mark: {member} has been warned, I couldn't DM them.")
            else:
              await ctx.send(f":white_check_mark: {member} has been warned.")  
        else:
          if member.id == 603635602809946113:
            return await ctx.send(f":x: You can't ban {member}!")
          elif member.id == 742388119516741642:
            return await ctx.send(":x: You can't warn me!")


def setup(client):
    client.add_cog(warn(client))