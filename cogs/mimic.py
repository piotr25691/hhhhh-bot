import discord
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from difflib import SequenceMatcher

class mimic(commands.Cog):
    # avatar command
    @commands.command(name="sayas")
    async def mimic(self, ctx, member: discord.Member=None, *, message=None):
        if member is None:
          return await ctx.send("Who are you trying to send a message as? :thinking:")
        if message is None:
          return await ctx.send(f"What message are you trying to send as {member}? :thinking:")  
        await ctx.message.delete() 
        hook = await ctx.channel.create_webhook(name=member.name, reason=f"User {ctx.author} used mimic")
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(
                hook.url,
                adapter=AsyncWebhookAdapter(session))
            if member.nick is None:    
                await webhook.send(message, username=member.name,
                               avatar_url=member.avatar_url)
            else:
                await webhook.send(message, username=member.nick,
                               avatar_url=member.avatar_url)
        await hook.delete()

def setup(client):
    client.add_cog(mimic(client))
