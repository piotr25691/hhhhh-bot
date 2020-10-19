import discord
from discord.ext import commands
import re
from vars import *

class say(commands.Cog):
    # say command (g doesnt work, dont try)
    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def say(self, ctx, *, body):
        # check if the message contains a g
        result = re.compile(r'\bg+\b', re.IGNORECASE).findall(body)
        # if a g is found do the following
        if result:
            if ctx.message.content == "hh!say fuck g":
                return await ctx.send(body)
            else:
                # reject the command and say the notification message
                # deletion is not required
                return await ctx.send('NO!')
        else:
            # delete message
            for word in tos:
                if word in ctx.message.content:
                    return await ctx.send("Absolutely not!\nAre you trying to get me banned?")
            await ctx.message.delete()
            # send the message
            return await ctx.send(body)

def setup(bot):
    bot.add_cog(say(bot))