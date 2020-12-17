import discord
from discord.ext import commands

class credits(commands.Cog):
    def __init__(self, client):
        self.client = client

    # avatar command
    @commands.command()
    async def credits(self, ctx):
        dev = await self.client.fetch_user(603635602809946113)
        special = [429935667737264139, 444550944110149633]
        special_thanks = ""
        for user in special:
          u = self.client.get_user(user)
          special_thanks = f"{special_thanks}{str(u)}\n"
        e = discord.Embed(title=':busts_in_silhouette: Credits', description="These people made <@!742388119516741642> possible. Let's applaud them!", color=discord.Colour.blurple())
        e.add_field(name="<:4228_discord_client_dev:727548651001348196> Developer", value=dev, inline=True)
        e.add_field(name=":star: Special Thanks", value=special_thanks, inline=True)
        e.add_field(name=":computer: Library Version", value=f"discord.py {discord.__version__}", inline=True)

        await ctx.send(embed=e)


        
def setup(client):
    client.add_cog(credits(client))