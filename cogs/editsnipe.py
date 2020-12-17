import discord
import datetime
from discord.ext import commands
global msg_
msg_ = None

class editsnipe(commands.Cog):
    @commands.Cog.listener()
    async def on_message_edit(self, ctx, message):
        if "hh!editsnipe" not in message.content:
            if not message.author.bot:
                global pfp
                pfp = message.author.avatar_url
                global server
                server = message.guild.name
                global msg_
                msg_ = message.content
                global author
                author = message.author
                global time
                compensation = datetime.timedelta(hours=1)
                time = datetime.datetime.now() + compensation
                time = str(time)[:19]
            else:
                pass

    @commands.command(name="editsnipe")
    async def editsnipe_(self, ctx):
        if  msg_ is not None:
            if server == ctx.guild.name:
                e = discord.Embed(description=msg_,
                                         color=discord.Colour.blurple())
                e.set_author(name=f'{author} said...', icon_url=pfp)
                e.set_footer(text=f"Messaqe edited at {time}")
                await ctx.send(embed=e)
            else:
                await ctx.send(":x: There is nothinq to snipe!")
        else:
            await ctx.send(":x: There is nothinq to snipe!")

def setup(client):
    client.add_cog(editsnipe(client))