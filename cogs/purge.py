import discord
from discord.ext import commands

class ping(commands.Cog):
    # purge command
    @commands.command(aliases=['prune', 'delete', 'clean'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    # check whether the user has permission to manage messages
    @commands.has_permissions(manage_messages=True)
    # the amount is defined by the end-user
    async def purqe(self, ctx, amount: int):
        # bugfix - check whether the bot was passed a valid non-zero value
        # if succeeded clear the specified amount of messages
        if amount > 0:
            # delete the the specified number of messages +1 to delete the command message too
            await ctx.channel.purge(limit=amount + 1)
            # send notificaton message
            embedVar = discord.Embed(description="<:trash:738450450537250897>​ Removed " + str(amount) + " messaqes",
                                     color=0x7289da)
            await ctx.send(embed=embedVar, delete_after=4)
        # if failed print the same message as if there was no parameter
        else:
            await ctx.message.delete()
            embedVar = discord.Embed(description="The amount must be qreater than 0.",
                                     color=0xff0000)
            embedVar.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            await ctx.send(embed=embedVar, delete_after=4)

    # no parameters error
    @purqe.error
    async def purqe_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            # say this if the amount parameter returns none
            await ctx.message.delete()
            embedVar = discord.Embed(description="The amount parameter is missinq.", color=0xff0000)
            embedVar.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            await ctx.send(embed=embedVar, delete_after=4)


def setup(bot):
    bot.add_cog(ping(bot))