import discord
from discord.ext import commands

class msgcount(commands.Cog):
    # messagecount command

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def msqcount(self, ctx, channel: discord.TextChannel = None):
        embedVar = discord.Embed(title="<a:wait:755401316142153778> Wait",
                                 description="Processinq channel...\nThis can take a very lonq time in biq channels.\nI'll pinq you when I'm finished.",
                                 color=0x7289da)
        await ctx.send(embed=embedVar, delete_after=15)
        with ctx.channel.typing():
            channel = channel or ctx.channel
            count = 0
            async for _ in channel.history(limit=None):
                count += 1
            embedVar = discord.Embed(
                                     description=f"There are {count} messaqes in {channel.mention}", color=0x7289da)
            embedVar.set_author(name='Results', icon_url="https://i.imgur.com/A8g1ViW.png")
            await ctx.send(ctx.author.mention, embed=embedVar)

def setup(bot):
    bot.add_cog(msgcount(bot))