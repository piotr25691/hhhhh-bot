import discord
from discord.ext import commands


class serverinfo(commands.Cog):
    @commands.command(name='serverinfo')
    async def guildinfo(self, ctx):
      online = 0
      idle = 0
      dnd = 0
      offline = 0
      for x in ctx.guild.members:
        if str(x.status) == "online":
          online+=1
        elif str(x.status) == "idle":
          idle+=1
        elif str(x.status) == "dnd":
          dnd+=1
        else:
          offline+=1
      stlist = [online, idle, dnd, offline]  
      e = discord.Embed(title=ctx.guild.name, color=discord.Colour.blurple())
      e.add_field(name="\u200b", value="**Server**", inline=False)
      e.add_field(name="ID", value=ctx.guild.id, inline=True)
      e.add_field(name="Owner", value=ctx.guild.owner.mention, inline=True)
      e.add_field(name="Channels", value=f'{sum([len(ctx.guild.text_channels), len(ctx.guild.voice_channels)])} ({len(ctx.guild.text_channels)} text, {len(ctx.guild.voice_channels)} voice)', inline=True)
      e.add_field(name="AFK Channel", value=ctx.guild.afk_channel, inline=True)
      e.add_field(name="Roles", value=len(ctx.guild.roles), inline=True)
      e.add_field(name="Region", value=ctx.guild.region, inline=True)
      e.add_field(name="Created on", value=str(ctx.guild.created_at)[:16], inline=True)
      if not ctx.guild.premium_tier == 0:
        e.add_field(name="Boost Tier", value=ctx.guild.premium_tier, inline=True)
      else:
        e.add_field(name="Boost Tier", value="Not Boosted", inline=True)  
      e.add_field(name="\u200b", value="**Members**", inline=False)
      e.add_field(name="Total Members", value=f"{len(ctx.guild.members)} (<:online:747395937625833552>{stlist[0]}<:idle:747395936766132234>{stlist[1]}<:dnd:747395937978286100>{stlist[2]}<:offline:747395931875573781>{stlist[3]} )", inline=True)
      e.add_field(name="Humans", value=len([x for x in ctx.guild.members if not x.bot]), inline=True)
      e.add_field(name="Bots", value=len([x for x in ctx.guild.members if x.bot]), inline=True)
      e.add_field(name="Verification Level", value=str(ctx.guild.verification_level).capitalize(), inline=True)
      e.set_thumbnail(url=ctx.guild.icon_url)

      await ctx.send(embed=e)


def setup(client):
  client.add_cog(serverinfo(client))
