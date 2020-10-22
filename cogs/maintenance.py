import discord
from discord.ext import commands
from main import prefixes
from PIL import Image

class maintenance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        error = getattr(error, 'original', error)
        # bot - nonexistent command
        if isinstance(error, commands.CommandNotFound):
            return

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            prefix = prefixes[f'{message.guild.id}']
        except KeyError:
            prefix = "hh!"


        if message.content.startswith(f'{prefix}'):
            if message.content == f'{prefix}restart':
                return
            if message.content == f'{prefix}reboot':
                return
            embedVar = discord.Embed(description="The bot is in maintenance mode.\nYou can't use any commands riqht now.",
                                 color=0xff0000)
            embedVar.set_author(name=f'Maintenance Mode', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await message.channel.send(embed=embedVar, delete_after=10)

        await self.bot.process_commands(message)


def setup(bot):
    bot.add_cog(maintenance(bot))