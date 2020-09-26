import discord
from discord.ext import commands

class react(commands.Cog):
    # react command
    @commands.command()
    async def react(self, ctx, *args):
        messageid = args[0]
        msgcontent = ctx.message.content
        emoji = str(msgcontent[28:])
        msg = await ctx.channel.fetch_message(messageid)
        try:
            await ctx.message.delete()
            return await msg.add_reaction(emoji)
        except discord.HTTPException:
            embedVar = discord.Embed(title=":x: Error", description="I can't access that emoji!", color=0xff0000)
            return await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(react(bot))