import discord
from discord.ext import commands
from discord.ext.commands.errors import CheckFailure
import inspect
import io
import textwrap
import traceback
import sys
from difflib import SequenceMatcher
from contextlib import redirect_stdout

admins = [603635602809946113, 444550944110149633, 429935667737264139, 350325552344858624]
token = ":no_entry: **NO!** I'm not leaking my token!"
tos = ["nigga", "nigger", "nigguh"]

class _eval(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='eval', hidden=True)
    # check whether the client owner executes the command or not
    async def _eval(self, ctx, *, body=None):
        if ctx.author.id in admins:
            if body is None:
              return await ctx.send("you need to give me code to execute dum dum")
            await ctx.message.delete()
            # evaluate and execute python code
            env = {
                'ctx': ctx,
                'client': self.client,
                'channel': ctx.channel,
                'author': ctx.author,
                'guild': ctx.guild,
                'message': ctx.message,
                'source': inspect.getsource,
                'TOKEN': token,
                'version': sys.version
            }

            ratio = round(SequenceMatcher(a=ctx.message.content, b="nigger").ratio(),1)
            if ratio >= 0.4:
              e = discord.Embed(title=":x: An exception has occurred", description="```You aren't allowed to use the n-word! ```", color=discord.Colour.from_rgb(255, 136, 0))
              e.set_footer(text="TOSBreakError")
              return await ctx.send(embed=e)
            
            def cleanup_code(content):
                if content.startswith('```') and content.endswith('```'):
                    return '\n'.join(content.split('\n')[1:-1])
                return content.strip('` \n')

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
                e = discord.Embed(title=":x: An exception has occurred", description=f"{err}", color=discord.Colour.from_rgb(255, 0, 0))
                e.set_footer(text=errtype)
                return await ctx.send(embed=e)
            func = env['func']
            try:
                with redirect_stdout(stdout):
                    ret = await func()
            except Exception as e:
                value = stdout.getvalue()
                err = f'```py\n{value}{traceback.format_exc()}```'
                errtype = e.__class__.__name__
            else:
                value = stdout.getvalue()
                if ret is None:
                    if value:
                        try:
                            out = f'```py\n{value}\n```'
                        except:
                            paginated_text = paginate(value)
                            for page in paginated_text:
                                if page == paginated_text[-1]:
                                    out = f'```py\n{page}\n```'
                                    break
                                await ctx.send(f'```py\n{page}\n```')
                else:
                    try:
                        out = f'```py\n{value}{ret}\n```'
                    except:
                        paginated_text = paginate(f"{value}{ret}")
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = f'```py\n{page}\n```'
                                break
                            await ctx.send(f'```py\n{page}\n```')
            if out:
                return await ctx.send(out)
            elif err:
                e = discord.Embed(title=":x: An exception has occurred", description=f"{err}", color=discord.Colour.from_rgb(255, 0, 0))
                e.set_footer(text=errtype) 
                return await ctx.send(embed=e)
            else:
                return
        else:
            raise CheckFailure("You are not allowed to use this command.")

def setup(client):
    client.add_cog(_eval(client))
