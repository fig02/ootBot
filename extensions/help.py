import discord
from discord.ext import commands

class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		await ctx.send('''
```
!help         list available commands

roles:
!roles        list available roles
!add          add one or more roles seperated by spaces
!remove       remove one or more roles seperated by spaces

gz:
!gz           link to the practice rom website
!manual       link to the practice rom manual
!gzemu        link to guide for enabling expansion pak in pj64
!watches      link to the common watches spreadsheet
!ultimate     link to the ultimate address spreadsheet

discords:
!rando        link to the randomizer server
!online       link to the OoT Online server
!modding      link to the hylian modding server
!glitchless   link to the glitchless server

faq:
!beginner     explanation of good categories to start with as a beginner
!cspointer    explanation of cs pointers for deku ww and how to fix it
!dekuspeed    explanation of deku ww loading zone speed
!essadapter   explanation of what an ESS adapter is and your options for getting one
!inputdisplay explanation of your options for getting an input display
!tutorials    link to Arthur's tutorial playlist
!hess         link to Arthur's HESS tutorial
!superslide   link to Arthur's superslide tutorial
!megasidehop  link to Arthur's megasidehop tutorial
!megaflip     link to Arthur's megaflip tutorial
!groundjump   link to Arthur's groundjump tutorial
!boatskip     link to Arthur's boat-key skip tutorial
!ganondoor    link to Mikami's deku-to-collapse wrong warp tutorial
!voidwarp     link to Sockfolder's child collapse voidwarp video
!instaclip    link to Zudu's instaclip tutorial
!rba          link to Dannyb's RBA explanation
!ba           link to Dannyb's BA explanation
!dotskip      links to Door of Time skip tutorials
!glitches     link to ZFG's glitch exhibition
!palwii       link to a walkthrough for getting OoT to run on PAL Wiis
!navi         Explanation of Navi's timer
!target       Explanation of targeting walls
```
		''')

def setup(bot):
	bot.add_cog(Help(bot))