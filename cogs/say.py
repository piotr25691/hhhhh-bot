import discord
from discord.ext import commands
import re

class say(commands.Cog):
    # say command (g doesnt work, dont try)
    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def say(self, ctx):
        # take the message content and save it inside a variable
        msgcontent = re.sub(f'hh!say', '', ctx.message.content)
        # check if the message contains a g
        result = re.compile(r'\bg+\b', re.IGNORECASE).findall(msgcontent)
        # if a g is found do the following
        if result:
            # reject the command and say the notification message
            # deletion is not required
            return await ctx.send('NO!')
        else:
            # delete message
            await ctx.message.delete()
            # send the message
            return await ctx.send(msgcontent)

def setup(bot):
    bot.add_cog(say(bot))