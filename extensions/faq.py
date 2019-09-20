import discord
from discord.ext import commands

class Faq(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def gz(self, ctx):
		await ctx.send(
'The Practice ROM can be downloaded here: \
<https://practicerom.com/>')
	
	@commands.command()
	async def manual(self, ctx):
		await ctx.send(
'Make sure to read the gz manual so you understand \
the tools you have available to you: \
<https://github.com/glankk/gz/blob/master/USAGE.md>')
	
	@commands.command()
	async def gzemu(self, ctx):
		await ctx.send(
'To use gz (or many other rom hacks) on PJ64 you \
need to change a couple settings.\n\
Pause the emulator with F2 shortly after starting the game \
or right click on the game in you games list to change settings.\n\
Guide: <https://imgur.com/a/bCdVV>')

	
def setup(bot):
	bot.add_cog(Faq(bot))