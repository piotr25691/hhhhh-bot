from discord.ext import commands

class purge(commands.Cog):
    @commands.command(aliases=['prune', 'delete', 'clean'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def purqe(self, ctx, amount: int=None):
        if amount is None:
          await ctx.send("How many messages are you purging? :thinking:")
        if amount > 0:
          await ctx.channel.purge(limit=amount+1)
        else:
          await ctx.send(f":x: It is impossible to purge {amount} messages!")


def setup(bot):
    bot.add_cog(purge(bot))  