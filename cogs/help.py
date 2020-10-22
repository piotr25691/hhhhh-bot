import discord
from discord.ext import commands
import json

class help(commands.Cog):
    with open("prefixes.json") as f:
        global prefixes
        prefixes = json.load(f)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx, *args):
        try:
            prefix = prefixes[f'{ctx.guild.id}']
        except KeyError:
            prefix = "hh!"
        # delete the message
        await ctx.message.delete()
        # define the big embed
        if len(args) == 0:
            embedVar = discord.Embed(
                                     description=f"All of the help topics for this bot live here.\n\n**Commands are split into separate cateqories. Please use `{prefix}help <cateqory>` with `<cateqory>` being one of the following options:**\n\n**Standard Commands**\n",
                                     color=0x7289da)
            embedVar.set_author(name='Help Topics', icon_url="https://i.imgur.com/A8g1ViW.png")
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            embedVar.add_field(name=":gear: Core", value="Standard commands.", inline=True)
            embedVar.add_field(name=":shield: Moderation", value="Moderation stuff.", inline=True)
            embedVar.add_field(name=":bangbang: BotAdmin", value="Bot admin and owner exclusive commands.\n", inline=True)
            embedVar.add_field(name="**Informational Commands**\n\n:information_source: Bot",
                               value="Bot information commands.", inline=True)
            embedVar.set_footer(text='Please pick a cateqory.')
            return await ctx.send(embed=embedVar)
        if args[0] == "core" or args[0] == "Core":
            embedVar = discord.Embed(description="These are the standard commands.",
                                     color=0x7289da)
            embedVar.set_author(name='Core Commands', icon_url="https://i.imgur.com/A8g1ViW.png")
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            embedVar.add_field(name=f"**{prefix}say <messaqe>**\nAdditional aliases: none",
                               value="Make the bot say anythinq you want.\n(except the forbidden letter of course!)", inline=True)
            embedVar.add_field(name=f"**{prefix}dm <member> <messaqe>**\nAdditional aliases: none",
                               value="DM anythinq to an user via the bot.\n(except the forbidden letter of course!)", inline=True)
            embedVar.add_field(name=f"**{prefix}h**\nAdditional aliases: none", value="H like a true hbot.", inline=True)
            embedVar.add_field(
                name=f"**{prefix}pinqeveryone**\nAdditional aliases:\n__{prefix}everyonepinq, {prefix}ateveryone__",
                value="Do a safe @everyone in an embed so no one qets pinqed.", inline=True)
            embedVar.add_field(name=f"**{prefix}pinq**\nAdditional aliases: none", value="Pinq the bot API.",
                               inline=True)
            embedVar.add_field(name=f"**{prefix}purqe <number>**\nAdditional aliases:\n__{prefix}prune, {prefix}delete, {prefix}clean__",
                               value="Purqe the messaqes in the channel you're in.\n It's that simple.", inline=True)
            embedVar.add_field(name=f"**{prefix}react <id> <emoji>**\nAdditional aliases: none",
                               value="React to a messaqe with an emoji of your choice via the bot.", inline=True)
            embedVar.add_field(name=f"**{prefix}math <number> <operation> <number>**\nAdditional aliases:\n__{prefix}calculate__",
                               value="Do math!", inline=True)
            embedVar.add_field(name=f"**{prefix}msqcount [channel]**\nAdditional aliases: none",
                               value="Compute the amount of messaqes in a channel.", inline=True)
            embedVar.add_field(name=f"**{prefix}snipe**\nAdditional aliases: none",
                               value="See the recently deleted messaqe.", inline=True)
            embedVar.add_field(name=f"**{prefix}editsnipe**\nAdditional aliases: none",
                               value="See the recently edited messaqe.", inline=True)
            embedVar.add_field(name=f"**{prefix}prefix**\nAdditional aliases: none",
                               value="Set the bot prefix.\n(Notice: - substitutes for a space at the end.)", inline=True)
            embedVar.set_footer(text='[] indicates parameters that are not required. <> indicates required parameters.')
            return await ctx.send(embed=embedVar)
        elif args[0] == "moderation" or args[0] == "Moderation":
            embedVar = discord.Embed(description="These are the moderation commands.",
                                     color=0x7289da)
            embedVar.set_author(name='Moderation Commands', icon_url="https://i.imgur.com/A8g1ViW.png")
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            embedVar.add_field(name="__**Moderation**__", value=f"These are the moderation commands that this bot has.",
                               inline=False)
            embedVar.add_field(name=f"**{prefix}ban <member>**\nAdditional aliases: none", value="Ban a member.", inline=True)
            embedVar.add_field(name=f"**{prefix}unban <member>**\nAdditional aliases: none",
                               value="Reverse a ban for someone.", inline=True)
            embedVar.add_field(name=f"**{prefix}kick <member>**\nAdditional aliases: none", value="Kick a member.",
                               inline=True)
            embedVar.add_field(name=f"**{prefix}warn <member> [reason]**\nAdditional aliases: none",
                               value="Warn someone.", inline=True)
            embedVar.set_footer(
                text='[]hh!h indicates parameters that are not required. <> indicates required parameters.')
            return await ctx.send(embed=embedVar)
        elif args[0] == "botadmin" or args[0] == "BotAdmin":
            embedVar = discord.Embed(
                                     description="These commands can only be executed by the owner (<@!603635602809946113>) or bot admins.",
                                     color=0x7289da)
            embedVar.set_author(name='Owner/Admin Only Commands', icon_url="https://i.imgur.com/A8g1ViW.png")
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            embedVar.add_field(name=f"**{prefix}eval <code>**\nAdditional aliases: none",
                               value="Processes and executes code.", inline=True)
            embedVar.add_field(name=f"**{prefix}die**\nAdditional aliases:\n__hh!kill, hh!stop__",
                               value="Terminate the bot from chat.", inline=True)
            embedVar.set_footer(text='[] indicates parameters that are not required. <> indicates required parameters.')
            return await ctx.send(embed=embedVar)
        elif args[0] == "bot" or args[0] == "Bot":
            embedVar = discord.Embed(title="Bot Information Commands",
                                     description="These commands let you qet bot information.", color=0x7289da)
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            embedVar.add_field(name=f"**{prefix}help**\nAdditional aliases: none", value="Display this messaqe.", inline=True)
            embedVar.add_field(name=f"**{prefix}info**\nAdditional aliases: none", value="Display the bot information.",
                               inline=True)
            embedVar.add_field(name=f"**{prefix}version**\nAdditional aliases: none",
                               value="Display the bot version information", inline=True)
            embedVar.add_field(name=f"**{prefix}invite**\nAdditional aliases: none", value="Invite the bot.", inline=True)
            embedVar.add_field(name=f"**{prefix}chanqeloq**\nAdditional aliases: none", value="See the bot chanqeloq.", inline=True)
            embedVar.set_footer(text='[] indicates parameters that are not required. <> indicates required parameters.')
            return await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(
                                     description=f":x: **That is not a valid cateqory.\nPlease use `{prefix}help` to view the cateqories.**",
                                     color=0x7289da)
            embedVar.set_author(name='Help Topics', icon_url="https://i.imgur.com/A8g1ViW.png")
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            return await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(help(bot))