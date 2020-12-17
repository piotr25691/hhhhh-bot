import discord
from discord.ext import commands


class avatar(commands.Cog):
    # avatar command
    @commands.command(aliases=['pfp'])
    async def avatar(self, ctx, member:discord.Member=None):
      if member is None:
        return await ctx.send("Whose profile picture are you trying to get? :thinking:")
      e = discord.Embed(title=f"Avatar of {member}", description=f"Show in browser\n[Click]({member.avatar_url})", color=discord.Colour.blurple())
      e.set_image(url=member.avatar_url)
      await ctx.send(embed=e)


def setup(client):
  client.add_cog(avatar(client))
