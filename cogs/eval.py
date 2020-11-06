import discord
from discord.ext import commands
from discord.ext.commands.errors import CheckFailure
import inspect
import io
import textwrap
import traceback
import sys
import time
import math
from contextlib import redirect_stdout
admins = [603635602809946113, 444550944110149633, 429935667737264139, 350325552344858624]
token_msgs = ["hh!eval token", "hh!eval TOKEN", "hh!e token", "hh!e TOKEN", "hh!evaluate token", "hh!evaluate TOKEN"]
token = ":no_entry: **NO!** I'm not leaking my token!"
tos = ["nigga", "nigger", "nigguh"]
class _eval(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.author.id == 742388119516741642:
        global message_c
        if not message.content.startswith("```py\n"):
          message_c = message.content
        else:
          message_c = message.content.replace("```py\n", "")
          message_c = message_c.replace("\n```", "")

    @commands.command(aliases=['e', 'eval', 'evaluate'])
    # check whether the bot owner executes the command or not
    async def _eval(self, ctx, *, body):
        if ctx.author.id in admins: 
            start = time.time()
            await ctx.message.delete()
            # evaluate and execute python code
            env = {
                'ctx': ctx,
                'bot': self.bot,
                'channel': ctx.channel,
                'author': ctx.author,
                'guild': ctx.guild,
                'message': ctx.message,
                'source': inspect.getsource,
                'TOKEN': token,
                'version': sys.version
            }
            if "config.json" in ctx.message.content:
                embedVar = discord.Embed(title=":x: An exception has occurred", description="```py\nYou aren't allowed to leak my token! ```", color=0xff0000)
                embedVar.set_footer(text="TokenLeakError")
                return await ctx.send(embed=embedVar)

            for word in tos:
                if word in ctx.message.content:
                    embedVar = discord.Embed(title=":x: An exception has occurred", description="```py\nYou aren't allowed to use the n-word! ```", color=0xff0000)
                    embedVar.set_footer(text="TOSBreakError")
                    return await ctx.send(embed=embedVar)
            
            def cleanup_code(content):
                if content.startswith('```') and content.endswith('```'):
                    return '\n'.join(content.split('\n')[1:-1])
                return content.strip('` \n')

            def get_syntax_error(e):
                if e.text is None:
                    return f'```py\n{e.__class__.__name__}: {e}\n```'
                return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

            env.update(globals())
            body = cleanup_code(body)
            stdout = io.StringIO()
            err = out = None
            to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

            def paginate(text: str):
                last = 0
                pages = []
                for curr in range(0, len(text)):
                    if curr % 1980 == 0:
                        pages.append(text[last:curr])
                        last = curr
                        appd_index = curr
                if appd_index != len(text) - 1:
                    pages.append(text[last:curr])
                return list(filter(lambda a: a != '', pages))

            try:
                exec(to_compile, env)
            except Exception as e:
                err = f'```py\n{e} ```'
                errtype = e.__class__.__name__
                embedVar = discord.Embed(title=":x: An exception has occurred", description=f"{err}", color=0xff0000)
                embedVar.set_footer(text=errtype)
                return await ctx.send(embed=embedVar)
            func = env['func']
            try:
                with redirect_stdout(stdout):
                    ret = await func()
            except Exception as e:
                value = stdout.getvalue()
                err = f'```py\n{value}{e} \n```'
                errtype = e.__class__.__name__
            else:
                value = stdout.getvalue()
                if ret is None:
                    if value:
                        try:
                            out = await ctx.send(f'```py\n{value}\n```')
                        except:
                            paginated_text = paginate(value)
                            for page in paginated_text:
                                if page == paginated_text[-1]:
                                    out = f'```py\n{page}\n```'
                                    break
                                await ctx.send(f'```py\n{page}\n```')
                else:
                    try:
                        out = await ctx.send(f'```py\n{value}{ret}\n```')
                    except:
                        paginated_text = paginate(f"{value}{ret}")
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = f'```py\n{page}\n```'
                                break
                            await ctx.send(f'```py\n{page}\n```')
                if out == None:
                  out = "Empty Response"
                end = time.time() 
                user = await self.bot.fetch_user(ctx.author.id)
                embedVar = discord.Embed(title="Processing results", description=f"Processed in {math.trunc((end-start)*100)} ms", color=0x7289da)
                embedVar.add_field(name="Input", value=f"```py\n{body}```", inline=False)
                embedVar.add_field(name="Output", value=f"```py\n{message_c}```", inline=False)
                return await user.send(embed=embedVar)
            if out:
                await ctx.send(out)
            elif err:
                embedVar = discord.Embed(title=":x: An exception has occurred", description=f"{err}", color=0xff0000)
                embedVar.set_footer(text=errtype)
                return await ctx.send(embed=embedVar)
            else:
                return
        else:
            raise CheckFailure("You are not allowed to use this command.")

def setup(bot):
    bot.add_cog(_eval(bot))
