import discord
from discord.ext import commands

class avatar(commands.Cog):
    # avatar command
    @commands.command(aliases=['pfp'])
    async def avatar(self, ctx, *, member: discord.Member = None):
        avatar_uri = member.avatar_url
        embedVar = discord.Embed(title="Avatar", description=f"Avatar of {member}", color=0x7289da)
        embedVar.add_field(name="Show in browser", value=f"[Link]({avatar_uri})")
        embedVar.set_image(url=f"{avatar_uri}")
        return await ctx.send(embed=embedVar)
        
def setup(bot):
    bot.add_cog(avatar(bot))