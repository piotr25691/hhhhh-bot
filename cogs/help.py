import discord
from discord.ext import commands
import json
import DiscordUtils

class help(commands.Cog):
    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx):
      with open("prefixes.json") as f:
          prefixes = json.load(f)
      try:
          prefix = prefixes[f'{ctx.guild.id}']
      except KeyError:
          prefix = "hh!"  
      embed1 = discord.Embed(
                                     description=f"All of the help topics for this bot live here.\n\n**Commands are split into separate cateqories. Please use `{prefix}help <cateqory>` with `<cateqory>` being one of the following options:**\n\n**Standard Commands**\n",
                                     color=0x7289da)
      embed1.set_author(name='Help Topics', icon_url="https://i.imgur.com/A8g1ViW.png")
      embed1.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
      embed1.add_field(name=":gear: Core",value="Standard commands.", inline=True)
      embed1.add_field(name=":shield: Moderation", value="Moderation stuff.", inline=True)
      embed1.add_field(name=":bangbang: BotAdmin", value="Bot admin and owner exclusive commands.\n", inline=True)
      embed1.add_field(name="**Informational Commands**\n\n:information_source: Bot",
                               value="Bot information commands.", inline=True)
      embed1.set_footer(text='React with the emojis below to show different help topics.')
      embed2 = discord.Embed(description="These are the standard commands.",
                                     color=0x7289da)
      embed2.set_author(name='Core Commands', icon_url="https://i.imgur.com/A8g1ViW.png")
      embed2.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
      embed2.add_field(name=f"**{prefix}say <messaqe>**\nAdditional aliases: none",
                               value="Make the bot say anythinq you want.\n(except the forbidden letter of course!)", inline=True)
      embed2.add_field(name=f"**{prefix}dm <member> <messaqe>**\nAdditional aliases: none",
                               value="DM anythinq to an user via the bot.\n(except the forbidden letter of course!)", inline=True)
      embed2.add_field(name=f"**{prefix}h**\nAdditional aliases: none", value="H like a true hbot.", inline=True)
      embed2.add_field(
                name=f"**{prefix}pinqeveryone**\nAdditional aliases:\n__{prefix}everyonepinq, {prefix}ateveryone__",
                value="Do a safe @everyone in an embed so no one qets pinqed.", inline=True)
      embed2.add_field(name=f"**{prefix}pinq**\nAdditional aliases: none", value="Pinq the bot API.",
                               inline=True)
      embed2.add_field(name=f"**{prefix}purqe <number>**\nAdditional aliases:\n__{prefix}prune, {prefix}delete, {prefix}clean__",
                               value="Purqe the messaqes in the channel you're in.\n It's that simple.", inline=True)
      embed2.add_field(name=f"**{prefix}react <id> <emoji>**\nAdditional aliases: none",
                               value="React to a messaqe with an emoji of your choice via the bot.", inline=True)
      embed2.add_field(name=f"**{prefix}math <number> <operation> <number>**\nAdditional aliases:\n__{prefix}calculate__",
                               value="Do math!", inline=True)
      embed2.add_field(name=f"**{prefix}msqcount [channel]**\nAdditional aliases: none",
                               value="Compute the amount of messaqes in a channel.", inline=True)
      embed2.add_field(name=f"**{prefix}snipe**\nAdditional aliases: none",
                               value="See the recently deleted messaqe.", inline=True)
      embed2.add_field(name=f"**{prefix}editsnipe**\nAdditional aliases: none",
                               value="See the recently edited messaqe.", inline=True)
      embed2.add_field(name=f"**{prefix}prefix**\nAdditional aliases: none",
                               value="Set the bot prefix.\n(Notice: - substitutes for a space at the end.)", inline=True)
      embed2.set_footer(text='[] indicates parameters that are not required. <> indicates required parameters.')
      embed3 = discord.Embed(description="These are the moderation commands.",
                                     color=0x7289da)
      embed3.set_author(name='Moderation Commands', icon_url="https://i.imgur.com/A8g1ViW.png")
      embed3.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
      embed3.add_field(name="__**Moderation**__", value=f"These are the moderation commands that this bot has.",
                               inline=False)
      embed3.add_field(name=f"**{prefix}ban <member>**\nAdditional aliases: none", value="Ban a member.", inline=True)
      embed3.add_field(name=f"**{prefix}unban <member>**\nAdditional aliases: none",
                               value="Reverse a ban for someone.", inline=True)
      embed3.add_field(name=f"**{prefix}kick <member>**\nAdditional aliases: none", value="Kick a member.",
                               inline=True)
      embed3.add_field(name=f"**{prefix}warn <member> [reason]**\nAdditional aliases: none",
                               value="Warn someone.", inline=True)
      embed3.set_footer(
                text='[]hh!h indicates parameters that are not required. <> indicates required parameters.')
      embed4 = discord.Embed(
                                     description="These commands can only be executed by the owner (<@!603635602809946113>) or bot admins.",
                                     color=0x7289da)
      embed4.set_author(name='Owner/Admin Only Commands', icon_url="https://i.imgur.com/A8g1ViW.png")
      embed4.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
      embed4.add_field(name=f"**{prefix}eval <code>**\nAdditional aliases: none",
                               value="Processes and executes code.", inline=True)
      embed4.add_field(name=f"**{prefix}sudo <command>**\nAdditional aliases: none",
                               value="Do a developer action.", inline=True)
      embed4.set_footer(text='[] indicates parameters that are not required. <> indicates required parameters.') 
      embed5 = discord.Embed(
                                     description="These commands let you qet bot information.", color=0x7289da)
      embed5.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
      embed5.add_field(name=f"**{prefix}help**\nAdditional aliases: none", value="Display this messaqe.", inline=True)
      embed5.add_field(name=f"**{prefix}info**\nAdditional aliases: none", value="Display the bot information.",
                               inline=True)
      embed5.add_field(name=f"**{prefix}version**\nAdditional aliases: none",
                               value="Display the bot version information", inline=True)
      embed5.add_field(name=f"**{prefix}invite**\nAdditional aliases: none", value="Invite the bot.", inline=True)
      embed5.add_field(name=f"**{prefix}chanqeloq**\nAdditional aliases: none", value="See the bot chanqeloq.", inline=True)
      embed5.set_footer(text='[] indicates parameters that are not required. <> indicates required parameters.')
      embed5.set_author(name='Bot Information Commands', icon_url="https://i.imgur.com/A8g1ViW.png")  
      paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
      paginator.add_reaction('⏪', "back")
      paginator.add_reaction('⏩', "next")
      paginator.add_reaction('🔐', "lock")
      embeds = [embed1, embed2, embed3, embed4, embed5]
      await paginator.run(embeds)

def setup(client):
    client.add_cog(help(client))