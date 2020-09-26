import discord
import re
from discord.ext import commands
from discord.ext.commands import Bot


class dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    # changelog command
    # dm command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dm(self, ctx, *args):
        userid = re.sub('[^0-9]', '', args[0])
        msgcontent = re.sub(f'hh!dm <@!{userid}>', '',
                            ctx.message.content)
        mobilemsgcontent = re.sub(f'hh!dm <@{userid}> --mobile', '', ctx.message.content)
        user = await self.bot.fetch_user(userid)
        await ctx.message.delete()
        if not "--mobile" in ctx.message.content:
            return await user.send(f'{msgcontent}')
        else:
            return await user.send(f'{mobilemsgcontent}')

def setup(bot):
    bot.add_cog(dm(bot))