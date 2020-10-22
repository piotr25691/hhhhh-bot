import discord
from discord.ext import commands

class react(commands.Cog):
    # react command
    @commands.command()
    async def react(self, ctx, *, body):
        messageid = body[:18]
        msgcontent = body[19:]
        emoji = str(msgcontent)
        msg = await ctx.channel.fetch_message(messageid)
        try:
            await ctx.message.delete()
            return await msg.add_reaction(emoji)
        except discord.HTTPException:
            embedVar = discord.Embed(description="I can't access that emoji!", color=0xff0000)
            embedVar.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(react(bot))