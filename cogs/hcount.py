from discord.ext import commands

class hcount(commands.Cog):
    @commands.command(name="hcount")
    async def hcount(self, ctx):
        await ctx.send(f"There have been {open('hcount.txt').read()} h's sent in total.")
def setup(client):
    client.add_cog(hcount(client))