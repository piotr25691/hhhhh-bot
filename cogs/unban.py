import discord
from discord.ext import commands

class unban(commands.Cog):
     # unban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unban(self, ctx, member:discord.Member=None):
        if member is None:
         return await ctx.send("Who are you unbanning? :thinking:")
        bans = await ctx.guild.bans()
        if member in bans:
          await ctx.send(f":white_check_mark: Successfully unbanned {member}!")
          return await ctx.guild.unban(discord.Object(id=member.id))
        else:
          await ctx.send(":x: I cannot unban that user, as that user is not banned!")


def setup(client):
    client.add_cog(unban(client))