import discord
from discord.ext import commands

class msgcount(commands.Cog):
    # messagecount command

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def msqcount(self, ctx, channel: discord.TextChannel=None):
        if channel is None:
          return await ctx.send("What channel are you trying to compute the count of messages in? :thinking:")
        e = discord.Embed(title=":gear: Wait",
                                 description="Processinq channel...\nThis can take a very lonq time in biq channels.\nI'll pinq you when I'm finished.",
                                 color=0x7289da)
        await ctx.send(embed=e, delete_after=15)
        with ctx.channel.typing():
            channel = channel or ctx.channel
            count = 0
            async for _ in channel.history(limit=None):
                count += 1
            e = discord.Embed(
                                     description=f"There are {count} messaqes in {channel.mention}", color=0x7289da)
            e.set_author(name='Results', icon_url="https://i.imgur.com/A8g1ViW.png")
            await ctx.send(ctx.author.mention, embed=e)

def setup(client):
    client.add_cog(msgcount(client))