import discord
from discord.ext import commands
from main import prefixes

class handler(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        error = getattr(error, 'original', error)
        # bot - nonexistent command
        if isinstance(error, commands.CommandNotFound):
            if maintenance == True:
                pass
            else:
                await ctx.message.delete()
                embedVar = discord.Embed(title=":x: Command Not Found", description="This command does not exist.",
                                         color=0xff0000)
                return await ctx.send(embed=embedVar, delete_after=10)
        # bot - command disabled
        if isinstance(error, commands.DisabledCommand):
            userid = ctx.message.author.id
            embedVar = discord.Embed(title=":x: Disabled", description="This command has been disabled.",
                                     color=0xff0000)
            return await ctx.send(embed=embedVar, delete_after=10)
        # bot - command on cooldown
        if isinstance(error, commands.CommandOnCooldown):
            embedVar = discord.Embed(title=":x: Ratelimited",
                                     description=f"You are ratelimited. Please try aqain in {math.ceil(error.retry_after)} seconds.",
                                     color=0xff0000)
            return await ctx.send(embed=embedVar, delete_after=10)
        # user - missing permissions
        if isinstance(error, commands.MissingPermissions):
            embedVar = discord.Embed(title=":x: Error", description=f"You can't use this command.", color=0xff0000)
            return await ctx.send(embed=embedVar, delete_after=10)
        # user - no DM
        if isinstance(error, commands.NoPrivateMessage):
            userid = ctx.message.author.id
            try:
                embedVar = discord.Embed(title=":x: Error", description=f"You can't use this command in DMs.",
                                         color=0xff0000)
                return await ctx.author.send(embed=embedVar, delete_after=10)
            except discord.Forbidden:
                pass
                return
        # user - no permission
        if isinstance(error, commands.CheckFailure):
            embedVar = discord.Embed(title=":x: Error", description=f"You can't use this command.", color=0xff0000)
            return await ctx.send(embed=embedVar, delete_after=10)


def setup(bot):
    bot.add_cog(handler(bot))