import discord
from discord.ext import commands

class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		await ctx.send('''
```
!help List available commands

roles:
!roles  > List available roles
!add    Add one or more roles seperated by spaces
!remove Remove one or more roles seperated by spaces

gz:
!gz       Link to the practice rom website
!manual   Link to the practice rom manual
!gzemu    Link to guide for enabling expansion pak in pj64
!watches  Link to the common watches spreadsheet
!ultimate Link to the ultimate address spreadsheet

discords:
!rando      Link to the randomizer server
!online     Link to the OoT Online server
!modding    Link to the hylian modding server
!glitchless Link to the glitchless server

faq:
!beginner    Explanation of good categories to start with as a beginner
!consoles    Explanation of what console is fastest for different categories
!cspointer   Explanation of cs pointers for deku ww and how to fix it
!dekuspeed   Explanation of deku ww loading zone speed
!fqcspointer Explanation of the cs pointer problem in faster quest
!capture     Explanation of different capture card options
!essadapter  Explanation of what an ESS adapter is and your options for getting one

```
		''')

def setup(bot):
	bot.add_cog(Help(bot))