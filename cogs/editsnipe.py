import discord
import datetime
from discord.ext import commands

class editsnipe(commands.Cog):
    @commands.Cog.listener()
    async def on_message_edit(self, message, *args):
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
                time = datetime.datetime.now()
                time = str(time)[:19]
            else:
                pass

    @commands.command(name="editsnipe")
    async def editsnipe_(self, ctx):
        if  msg_ is not None:
            if server == ctx.guild.name:
                embedVar = discord.Embed(description=msg_,
                                         color=0x7289da)
                embedVar.set_author(name=f'{author} said...', icon_url=pfp)
                embedVar.set_footer(text=f"Messaqe edited at {time}")
                await ctx.send(embed=embedVar)
            else:
                await ctx.send(":x: I have nothing to editsnipe!")
        else:
            await ctx.send(":x: I have nothing to editsnipe!")

def setup(bot):
    bot.add_cog(editsnipe(bot))
