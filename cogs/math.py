import discord
from discord.ext import commands
import math

class math(commands.Cog):
    # version command
    @commands.command(name='math')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def calculate(self, ctx, *args):
        value1 = float(args[0])
        value2 = float(args[2])
        operation = args[1]
        if value2 == 0 and operation == "/":
            return await ctx.send(":x: Cannot divide by zero")
        if operation == "+":
            floatresult = float(value1 + value2)
            result = int(value1 + value2)
            if not str(floatresult).endswith(".0"):
                await ctx.send(f"```{floatresult}```")
            else:
                await ctx.send(f"```{result}```")
        elif operation == "-":
            floatresult = float(value1 - value2)
            result = int(value1 - value2)
            if not str(floatresult).endswith(".0"):
                await ctx.send(f"`{floatresult}`")
            else:
                await ctx.send(f"```{result}```")
        elif operation == "*":
            floatresult = float(value1 * value2)
            result = int(value1 * value2)
            if not str(floatresult).endswith(".0"):
                await ctx.send(f"`{floatresult}`")
            else:
                await ctx.send(f"```{result}```")
        elif operation == "/":
            floatresult = float(value1 / value2)
            result = int(value1 / value2)
            if not str(floatresult).endswith(".0"):
                await ctx.send(f"```{floatresult}```")
            else:
                await ctx.send(f"```{result}```")
        else:
            return await ctx.send(":x: Invalid operation")

def setup(bot):
    bot.add_cog(math(bot))