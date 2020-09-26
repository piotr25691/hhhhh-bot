import discord
from discord.ext import commands

class h(commands.Cog):
    # h command
    @commands.command(name='h')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def letter(self, ctx):
        # send the h
        await ctx.message.delete()
        return await ctx.send('h')

def setup(bot):
    bot.add_cog(h(bot))