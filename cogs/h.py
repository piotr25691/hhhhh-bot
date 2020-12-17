from discord.ext import commands

class h(commands.Cog):
    # h command
    @commands.command(name='h')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def h(self, ctx):
        # send the h
        await ctx.send("h")

def setup(client):
    client.add_cog(h(client))