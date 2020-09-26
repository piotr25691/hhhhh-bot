import discord
from discord.ext import commands

class changelog(commands.Cog):
    # changelog command
    @commands.command(name='chanqeloq')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def changelog_(self, ctx):
        embedVar = discord.Embed(title="Bot Chanqeloq", description="See the new stuff added in!", color=0x7289da)
        embedVar.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
        embedVar.add_field(name="September 25th (1.1/b20200925)",
                           value="`hh!snipe` and `hh!editsnipe` were added. Now you can know what was that deleted/edited message!", inline=False)
        embedVar.add_field(name="September 21st (1.1/b20200921)",
                           value="An update to fully comply with Discord's TOS was released.", inline=False)
        embedVar.add_field(name="September 19th (1.1/b20200919)",
                           value="1.1 version was released!\nMajor coq revamps occurred, and the bot is now fully h-compliant!", inline=False)
        embedVar.add_field(name="September 18th (1.0c/b20200918)",
                           value="The bot is finally beinq hosted mostly 24/7!\nYou can now enjoy the functions of the bot to the fullest!", inline=False)
        embedVar.add_field(name="September 17th (1.0c/b20200917)",
                           value="1.0c version was released!\nMostly everythinq had been rebuilt by that point.", inline=False)
        embedVar.add_field(name="September 16th (1.0b/b20200916)",
                           value="The help command was revamped.\nNow it takes a cateqory rather than display everythinq at once.", inline=False)
        embedVar.add_field(name="More Changes", value="coming soon:tm:")
        return await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(changelog(bot))