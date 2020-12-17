from discord.ext import commands

class invite(commands.Cog):
    # changelog command
    @commands.command(name='invite')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invite_(self, ctx):
       await ctx.send("Invite me via this link:\nhttp://tiny.cc/hhhhh-invite")

def setup(client):
    client.add_cog(invite(client))