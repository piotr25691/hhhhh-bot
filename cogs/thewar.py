from discord.ext import commands

class thewar(commands.Cog):
    # the war
    @commands.command(name='the')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def thewar(self, ctx, *, body=None):
      if body is None:
        await ctx.send("war")
      elif body == "war":
        await ctx.send("the war")
      else:
        await ctx.send("YOU DUN FUCKED UP M8 THAT IS NOT THE WAR :rage::rage::rage::rage::rage:")
def setup(client):
    client.add_cog(thewar(client))