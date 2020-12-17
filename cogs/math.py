import discord
from discord.ext import commands
import re

class math(commands.Cog):
    # version command
    @commands.command(name='math')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def calculate(self, ctx, *, body=None):
        if body is None:
          return await ctx.send("What is your math problem? :thinking:")
        mathr = re.compile(r'^[0-9+\-*\/\(\)\.\%]*$', re.IGNORECASE).findall(body)
        
        if mathr:
          if re.compile(r'[.]{2,}', re.IGNORECASE).findall(body):
              return await ctx.send(":x: This math problem has invalid syntax and cannot be computed.")
        elif not mathr:
          return await ctx.send(f':x: This math problem contains an invalid character and cannot be computed.\nMake sure you do not use any invalid operators or expressions!')
        
        inp = re.sub(r"\.(?![0-9])","", body)
       
        try:
           eval_ = eval(inp, {'__builtins__':None})
        except SyntaxError:
           return await ctx.send(":x: This math problem has invalid syntax and cannot be computed.")
        if str(eval_).endswith(".0"):
          return await ctx.send(f"```{int(eval_)}```")    
        else:   
          return await ctx.send(f"```{eval_}```")

def setup(client):
    client.add_cog(math(client))