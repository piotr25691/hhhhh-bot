import discord
import datetime
from discord.ext import commands
global msg_
msg_ = None

class snipe(commands.Cog):
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if "hh!snipe" not in message.content:
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
                time = datetime.datetime.utcnow()
                time = str(time)[:19]
            else:
                pass

    @commands.command(name="snipe")
    async def snipe_(self, ctx):
        if msg_ is not None:
            if server == ctx.guild.name:
                embedVar = discord.Embed(description=msg_,
                                         color=0x7289da)
                embedVar.set_author(name=f'{author} said...', icon_url=f'{pfp}')
                embedVar.set_footer(text=f"Messaqe sent at {time}")
                await ctx.send(embed=embedVar)
            else:
                await ctx.send(":x: I have nothing to snipe!")
        else:
            await ctx.send(":x: I have nothing to snipe!")


def setup(bot):
    bot.add_cog(snipe(bot))
