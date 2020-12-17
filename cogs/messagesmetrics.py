import discord
from discord.ext import commands
import json
import datetime

class messaqes(commands.Cog):
    @commands.command(name='messaqes')
    async def messaqes(self, ctx):
        today = datetime.date.today()
        today_key = str(datetime.date.today()).replace("-", "")
        yesterday = today - datetime.timedelta(days=1)
        yesterday_key = str(yesterday).replace("-", "")
        prev2 = today - datetime.timedelta(days=2)
        prev2_key = str(prev2).replace("-", "")
        prev3 = today - datetime.timedelta(days=3)
        prev3_key = str(prev3).replace("-", "")
        prev4 = today - datetime.timedelta(days=4)
        prev4_key = str(prev4).replace("-", "")
        prev5 = today - datetime.timedelta(days=5)
        prev5_key = str(prev5).replace("-", "")
        prev6 = today - datetime.timedelta(days=6)
        prev6_key = str(prev6).replace("-", "")
        prev7 = today - datetime.timedelta(days=7)
        prev7_key = str(prev7).replace("-", "")
        with open("message_metric.json") as f:
            messages_data = json.load(f)
        try:
            messages = int(messages_data[today_key])
        except KeyError:
            messages = 0
        try:
            messages_yesterday = int(messages_data[yesterday_key])
        except KeyError:
            messages_yesterday = 0
        try:
            messages_prev2 = int(messages_data[prev2_key])
        except KeyError:
            messages_prev2 = 0
        try:
            messages_prev3 = int(messages_data[prev3_key])
        except KeyError:
            messages_prev3 = 0
        try:
            messages_prev4 = int(messages_data[prev4_key])
        except KeyError:
            messages_prev4 = 0
        try:
            messages_prev5 = int(messages_data[prev5_key])
        except KeyError:
            messages_prev5 = 0
        try:
            messages_prev6 = int(messages_data[prev6_key])
        except KeyError:
            messages_prev6 = 0
        try:
            messages_prev7 = int(messages_data[prev7_key])
        except KeyError:
            messages_prev7 = 0
        e = discord.Embed(title="Messaqes metrics", description=f"There have been {str(messages)} messaqes sent at {today}")
        e.add_field(name="Messaqes sent over the last 7 days", value=f"{yesterday}: {messages_yesterday}\n{prev2}: {messages_prev2}\n{prev3}: {messages_prev3}\n{prev4}: {messages_prev4}\n{prev5}: {messages_prev5}\n{prev6}: {messages_prev6}\n{prev7}: {messages_prev7}")

        await ctx.send(embed=e)


def setup(client):
    client.add_cog(messaqes(client))