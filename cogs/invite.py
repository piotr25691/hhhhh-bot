import discord
from discord.ext import commands

class invite(commands.Cog):
    # changelog command
    @commands.command(name='invite')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invite_(self, ctx):
        embedVar = discord.Embed(title=":incoming_envelope: Invite",
                                 description="**Invite the bot** [here](https://discord.com/oauth2/authorize?client_id=742388119516741642&scope=bot&permissions=8)",
                                 color=0x7289da)
        embedVar.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
        return await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(invite(bot))