import discord
from discord.ext import commands

with open("removed.txt") as f:
    removed = int(f.read().strip())

class help(commands.Cog):
    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx, *args):
        # delete the message
        await ctx.message.delete()
        # define the big embed
        if len(args) == 0:
            embedVar = discord.Embed(title="Help Topics",
                                     description="All of the help topics for this bot live here.\n\n**Commands are split into separate cateqories. Please use `hh!help <cateqory>` with `<cateqory>` being one of the following options:**\n\n**Standard Commands**\n",
                                     color=0x7289da)
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            embedVar.add_field(name=":gear: Core", value="Standard commands.", inline=True)
            embedVar.add_field(name=":shield: Moderation", value="Moderation stuff.", inline=True)
            embedVar.add_field(name=":bangbang: Owner", value="Owner exclusive commands.\n", inline=True)
            embedVar.add_field(name="**Informational Commands**\n\n:information_source: Bot",
                               value="Bot information commands.", inline=True)
            embedVar.set_footer(text='Please pick a cateqory.')
            return await ctx.send(embed=embedVar)
        if args[0] == "core" or args[0] == "Core":
            embedVar = discord.Embed(title="Core Commands", description="These are the standard commands.",
                                     color=0x7289da)
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            embedVar.add_field(name="**hh!say <messaqe>**\nAdditional aliases: none",
                               value="Make the bot say anythinq you want.\n(except the forbidden letter of course!)", inline=True)
            embedVar.add_field(name="**hh!dm <member> [--mobile] <messaqe>**\nAdditional aliases: none",
                               value="DM anythinq to an user via the bot.\n(except the forbidden letter of course!)", inline=True)
            embedVar.add_field(name="**hh!h**\nAdditional aliases: none", value="H like a true hbot.", inline=True)
            embedVar.add_field(
                name="**hh!pinqeveryone [--unsafe]**\nAdditional aliases:\n__hh!everyonepinq, hh!ateveryone__",
                value="Pinq @everyone safely! (or unsafely dependinq on the arquments)", inline=True)
            embedVar.add_field(name="**hh!pinq**\nAdditional aliases: none", value="Pinq the bot API.",
                               inline=True)
            embedVar.add_field(name="**hh!purqe <number>**\nAdditional aliases:\n__hh!prune, hh!delete, hh!clean__",
                               value="Purqe the messaqes in the channel you're in.\n It's that simple.", inline=True)
            embedVar.add_field(name="**hh!react <id> <emoji>**\nAdditional aliases: none",
                               value="React to a messaqe with an emoji of your choice via the bot.", inline=True)
            embedVar.add_field(name="**hh!math <number> <operation> <number>**\nAdditional aliases:\n__hh!calculate__",
                               value="Do math!", inline=True)
            embedVar.add_field(name="**hh!msqcount [channel]**\nAdditional aliases: none",
                               value="Compute the amount of messaqes in a channel.", inline=True)
            embedVar.add_field(name="**hh!snipe**\nAdditional aliases: none",
                               value="See the recently deleted messaqe.", inline=True)
            embedVar.add_field(name="**hh!editsnipe**\nAdditional aliases: none",
                               value="See the recently edited messaqe.", inline=True)
            embedVar.set_footer(text='[] indicates parameters that are not required. <> indicates required parameters.')
            return await ctx.send(embed=embedVar)
        elif args[0] == "moderation" or args[0] == "Moderation":
            embedVar = discord.Embed(title="Moderation Commands", description="These are the moderation commands.",
                                     color=0x7289da)
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            embedVar.add_field(name="__**Moderation**__", value=f"These are the moderation commands that this bot has.",
                               inline=False)
            embedVar.add_field(name="**hh!ban <member>**\nAdditional aliases: none", value="Ban a member.", inline=True)
            embedVar.add_field(name="**hh!unban <member>**\nAdditional aliases: none",
                               value="Reverse a ban for someone.", inline=True)
            embedVar.add_field(name="**hh!kick <member>**\nAdditional aliases: none", value="Kick a member.",
                               inline=True)
            embedVar.add_field(name="**hh!warn <member> [--mobile] [reason]**\nAdditional aliases: none",
                               value="Warn someone.", inline=True)
            embedVar.set_footer(
                text='[]hh!h indicates parameters that are not required. <> indicates required parameters.')
            return await ctx.send(embed=embedVar)
        elif args[0] == "owner" or args[0] == "Owner":
            embedVar = discord.Embed(title="Owner Only Commands",
                                     description="These commands can only be executed by the owner of the bot:\n<@!603635602809946113>.",
                                     color=0x7289da)
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            embedVar.add_field(name="**hh!eval <code>**\nAdditional aliases: none",
                               value="Processes and executes code.", inline=True)
            embedVar.add_field(name="**hh!die**\nAdditional aliases:\n__hh!kill, hh!stop__",
                               value="Terminate the bot from chat.", inline=True)
            embedVar.set_footer(text='[] indicates parameters that are not required. <> indicates required parameters.')
            return await ctx.send(embed=embedVar)
        elif args[0] == "bot" or args[0] == "Bot":
            embedVar = discord.Embed(title="Bot Information Commands",
                                     description="These commands let you qet bot information.", color=0x7289da)
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            embedVar.add_field(name="**hh!help**\nAdditional aliases: none", value="Display this messaqe.", inline=True)
            embedVar.add_field(name="**hh!info**\nAdditional aliases: none", value="Display the bot information.",
                               inline=True)
            embedVar.add_field(name="**hh!version**\nAdditional aliases: none",
                               value="Display the bot version information", inline=True)
            embedVar.add_field(name="**hh!invite**\nAdditional aliases: none", value="Invite the bot.", inline=True)
            embedVar.add_field(name="**hh!chanqeloq**\nAdditional aliases: none", value="See the bot chanqeloq.", inline=True)
            embedVar.set_footer(text='[] indicates parameters that are not required. <> indicates required parameters.')
            return await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title="Help Topics",
                                     description=":x: **That is not a valid cateqory.\nPlease use `hh!help` to view the cateqories.**",
                                     color=0x7289da)
            embedVar.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/742388119516741642/0547c1220f0ed953aee67751730d37e0.webp?size=1024")
            return await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(help(bot))