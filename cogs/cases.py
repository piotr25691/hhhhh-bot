import discord
from discord.ext import commands
import corona_python


class corona(commands.Cog):
    @commands.command()
    async def corona(self, ctx, *, country=None):
      world = corona_python.World()
      if country is None:
        return await ctx.send("What country are you trying to get COVID-19 stats of? :thinking:")
      ccountry = country.capitalize()
      ccountry = corona_python.Country(ccountry)
      if not country.lower() == "world": 
        try:
          e = discord.Embed(title=f"COVID-19 stats for {country.capitalize()} :flushed:")
          e.add_field(name="Cases (total):", value=ccountry.total_cases(), inline=True)
          e.add_field(name="Cases (today):", value=ccountry.today_cases(), inline=True)
          e.add_field(name="Deaths (total):", value=ccountry.total_deaths(), inline=True)
          e.add_field(name="Deaths (today):", value=ccountry.today_deaths(), inline=True)
          e.add_field(name="Deaths (total):", value=ccountry.total_deaths(), inline=True)
          e.add_field(name="Recovered (today):", value=ccountry.today_recovered(), inline=True)
          e.add_field(name="Recovered (total):", value=ccountry.recovered(), inline=True)
          e.add_field(name="Active cases:", value=ccountry.active(), inline=True)
          e.add_field(name="Critical cases:", value=ccountry.critical(), inline=True)
          e.add_field(name="Cases/1000000 people:", value=ccountry.cases_per_one_million(), inline=True)
          e.add_field(name="Deaths/1000000 people:", value=ccountry.deaths_per_one_million(), inline=True)
          e.add_field(name="Tests (total):", value=ccountry.total_tests(), inline=True)
          e.add_field(name="Tests/1000000 people::", value=ccountry.tests_per_one_million(), inline=True)
          return await ctx.send(embed=e)
        except KeyError:
          return await ctx.send(f":x: There is no country named `{country}`, or there's no data available for it!")   
      else:
        e = discord.Embed(title=f"Worldwide COVID-19 stats :flushed:")
        e.add_field(name="Cases (total):", value=world.total_cases(), inline=True)
        e.add_field(name="Cases (today):", value=world.today_cases(), inline=True)
        e.add_field(name="Deaths (total):", value=world.total_deaths(), inline=True)
        e.add_field(name="Deaths (today):", value=world.today_deaths(), inline=True)
        e.add_field(name="Deaths (total):", value=world.total_deaths(), inline=True)
        e.add_field(name="Recovered (today):", value=world.today_recovered(), inline=True)
        e.add_field(name="Recovered (total):", value=world.recovered(), inline=True)
        e.add_field(name="Active cases:", value=world.active_cases(), inline=True)
        e.add_field(name="Critical cases:", value=world.critical_cases(), inline=True)
        e.add_field(name="Cases/1000000 people:", value=world.cases_per_one_million(), inline=True)
        e.add_field(name="Deaths/1000000 people:", value=world.deaths_per_one_million(), inline=True)
        e.add_field(name="Tests (total):", value=world.total_tests(), inline=True)
        return await ctx.send(embed=e)  
       


def setup(client):
    client.add_cog(corona(client))