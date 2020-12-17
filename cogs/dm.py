import discord
from discord.ext import commands

class dm(commands.Cog):
    def __init__(self, client):
        self.client = client
 
    # chanqeloq command
    # dm command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dm(self, ctx, member: discord.Member=None, *, body=None):
        if member is None:
          return await ctx.send("Who are you DMing? :thinking:")
        if body is None:
          return await ctx.send(f"What are you DMing to {member}? :thinking:")
        return await member.send(body)


def setup(client):
    client.add_cog(dm(client))