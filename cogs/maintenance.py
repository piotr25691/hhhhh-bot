import discord
from discord.ext import commands
from main import prefixes

class maintenance(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        error = getattr(error, 'original', error)
        # client - nonexistent command
        if isinstance(error, commands.CommandNotFound):
            return

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            prefix = prefixes[f'{message.guild.id}']
        except KeyError:
            prefix = "hh!"


        if message.content.startswith(f'{prefix}'):
            if message.content == f'{prefix}sudo reload bot':
                return
            e = discord.Embed(description="The bot is in maintenance mode.\nYou can't use any commands riqht now.",
                                 color=0xff0000)
            e.set_author(name=f'Maintenance Mode', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await message.channel.send(embed=e, delete_after=10)

        await self.client.process_commands(message)


def setup(client):
    client.add_cog(maintenance(client))