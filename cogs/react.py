import discord
from discord.ext import commands

class react(commands.Cog):
    # react command
    @commands.command()
    async def react(self, ctx, id, *, body):
        emoji = str(body)
        msg = await ctx.channel.fetch_message(id)
        try:
            return await msg.add_reaction(emoji)
        except discord.HTTPException:
            e = discord.Embed(description="I can't access that emoji!", color=0xff0000)
            e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(react(bot))