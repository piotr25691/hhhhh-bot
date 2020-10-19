import discord
from discord.ext import commands
from discord.ext.commands.errors import CheckFailure
import inspect
import io
import textwrap
import ast
import traceback
import sys
import json
from contextlib import redirect_stdout
admins = [603635602809946113, 444550944110149633, 429935667737264139, 350325552344858624]
token_msgs = ["hh!eval token", "hh!eval TOKEN", "hh!e token", "hh!e TOKEN", "hh!evaluate token", "hh!evaluate TOKEN"]
token = ":no_entry: **NO!** I'm not leaking my token!"
tos = ["nigga", "nigger", "nigguh"]
class _eval(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['e', 'eval', 'evaluate'])
    # check whether the bot owner executes the command or not
    async def _eval(self, ctx, *, body):
        if ctx.author.id in admins:
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
            if ctx.message.content in token_msgs:
                return await ctx.send(token)

            if "config.json" in ctx.message.content:
                err = await ctx.send(":no_entry: **NO!** I'm not leaking my token!")
                return

            for word in tos:
                if word in ctx.message.content:
                    err = await ctx.send("Absolutely not!\nAre you trying to get me banned?")
                    return

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
                err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
                return
            func = env['func']
            try:
                with redirect_stdout(stdout):
                    ret = await func()
            except Exception as e:
                value = stdout.getvalue()
                err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
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
                                    out = await ctx.send(f'```py\n{page}\n```')
                                    break
                                await ctx.send(f'```py\n{page}\n```')
                else:
                    try:
                        out = await ctx.send(f'```py\n{value}{ret}\n```')
                    except:
                        paginated_text = paginate(f"{value}{ret}")
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.send(f'```py\n{page}\n```')
                                break
                            await ctx.send(f'```py\n{page}\n```')
            # when finished remove the command message
            if out:
                return
            elif err:
                return
            else:
                return
        else:
            raise CheckFailure("You are not allowed to use this command.")

def setup(bot):
    bot.add_cog(_eval(bot))