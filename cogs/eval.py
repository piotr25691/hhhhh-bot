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
import time
import math
import asyncio
from contextlib import redirect_stdout
admins = [603635602809946113, 444550944110149633, 429935667737264139, 350325552344858624]
token_msgs = ["hh!eval token", "hh!eval TOKEN", "hh!e token", "hh!e TOKEN", "hh!evaluate token", "hh!evaluate TOKEN"]
token = ":no_entry: **NO!** I'm not leaking my token!"
errors = ['Traceback', 'Error']
class _eval(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if "NzQyMzg4MTE5NTE2NzQxNjQy.XzFY0A.vm9GqsW-z_VLolu-kLCKNK6KSyY" in message.content:
                await message.delete()
                await message.channel.send(":no_entry: **NO!** I'm not leaking my token!")
            if message.author.bot:
                output = message.content
                with open("eval.txt", "w") as f:
                    f.write(output)
                    await asyncio.sleep(1)
                    f.write("")
                    f.close()
            else:
                pass
        except UnicodeEncodeError:
            pass

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
            if ctx.message.content in token_msgs:
                err = await ctx.send(token)
                return

            if "config.json" in ctx.message.content:
                err = await ctx.send(":no_entry: **NO!** I'm not leaking my token!")
                return



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
                with open("eval.txt", "w") as f:
                    f.write(f'```py\n{e.__class__.__name__}: {e}\n```')
                    f.close()
                return
            func = env['func']
            try:
                with redirect_stdout(stdout):
                    ret = await func()
            except Exception as e:
                value = stdout.getvalue()
                with open("eval.txt", "w") as f:
                    f.write(f'```py\n{value}{traceback.format_exc()}\n```')
                    f.close()
            else:
                value = stdout.getvalue()
                if ret is None:
                    if value:
                        try:
                            with open("eval.txt", "w") as f:
                                f.write(f'```py\n{value}\n```')
                                f.close()
                        except:
                            paginated_text = paginate(value)
                            for page in paginated_text:
                                if page == paginated_text[-1]:
                                    with open("eval.txt", "w") as f:
                                        f.write(f'```py\n{page}\n```')
                                        f.close()
                                    break
                                with open("eval.txt", "w") as f:
                                    f.write(f'```py\n{page}\n```')
                                    f.close()
                else:
                    try:
                        with open("eval.txt", "w") as f:
                            f.write(f'```py\n{value}{ret}\n```')
                            f.close()
                    except:
                        paginated_text = paginate(f"{value}{ret}")
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                with open("eval.txt", "w") as f:
                                    f.write(f'```py\n{page}\n```')
                                    f.close()
                                break
                            with open("eval.txt", "w") as f:
                                f.write(f'```py\n{page}\n```')
                                f.close()

            end = time.time()
            with open("eval.txt") as f:
                output = str(f.read().strip())
            if output == "":
                output = str(None)
        
            embedVar = discord.Embed(title="Evaluation Results", description=f"Processed in {math.trunc((end-start)*1000)} ms")
            embedVar.add_field(name="Input", value=f"```{str(body)}```", inline=False)
            embedVar.add_field(name="Output", value=f"```{output.strip('```').lstrip('py')}```", inline=False)
            return await ctx.send(embed=embedVar)
        else:
            raise CheckFailure("You are not allowed to use this command.")

def setup(bot):
    bot.add_cog(_eval(bot))