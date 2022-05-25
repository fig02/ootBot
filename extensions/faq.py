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
<https://practicerom.com/manual/>')

	@commands.command()
	async def gzemu(self, ctx):
		await ctx.send(
'To use gz (or many other rom hacks) on PJ64 you \
need to change a couple settings.\n\
Pause the emulator with F2 shortly after starting the game \
or right click on the game in your games list to change settings.\n\
Guide: <https://imgur.com/a/bCdVV>')

	@commands.command()
	async def watches(self, ctx):
		await ctx.send(
'To see values from RAM in the Practice ROM, you need to use the Watches menu.\n\
Address and flags list: <https://bthl.es/0f>\n\
Import common watches to gz by placing a file on your SD card: <https://pastebin.com/C7qczFia>\n\
')

	@commands.command()
	async def ultimate(self, ctx):
		await ctx.send(
'The ultimate spreadsheets are more comprehensive than the general sheet. There are 2 versions. \n\
This sheet is less complete but has the other versions: <https://bthl.es/0g> \n\
This sheet is more up to date but only has debug and 1.0: <https://bthl.es/0h>')

	@commands.command()
	async def rando(self, ctx):
		await ctx.send(
'This server is for speedrunning Ocarina of Time. \n\
For any Item Randomizer related questions please join this server here: https://discord.gg/eebmyE9')

	@commands.command()
	async def online(self, ctx):
		await ctx.send(
'Join this server here for OoT Online: https://discordapp.com/invite/UFVY9DE')

	@commands.command()
	async def modding(self, ctx):
		await ctx.send(
'Join this server here for OoT and MM ROM Hacking: https://discord.gg/BwekbEU')

	@commands.command()
	async def glitchless(self, ctx):
		await ctx.send(
'This server has more channels dedicated to learning glitchless categories: https://discordapp.com/invite/MeeMcZU')

	@commands.command()
	async def beginner(self, ctx):
		await ctx.send(
'As a beginner you have many options to start running this game. Here are some common suggestions: \n\n\
GSR - This category is very commonly recommended to beginners. It involves completing Shadow, Spirit, \
and doing most of Forest before beating the game. The category will teach you a lot of fundamentals that will \
carry over to more advanced categories. A common downside cited about this category is mainly the amount of \
cutscenes you have to sit through. There is a tutorial in the resources section.\n\n\
No Wrong Warp (SRM) - This run is a good introduction to SRM. It\'s comprised of doing LightNode SRM to gain control \
during the title screen to become adult with a ton of items available in the game. Within a few minutes of starting \
the game, you\'re able to go and open the rainbow bridge and beat Ganon.\n\n\
Glitchless - This category is great to start with because it focuses more on movement than anything else. \
This lays the groundwork for being fast at other categories. A 4 hour run is pretty long for beginners, but \
if you are okay with the length, this is another great starting point. For obvious reasons, this category \
has a lot of cutscenes too. Join the glitchless discord for more help centered around specifically glitchless. \n\n\
Defeat Ganon (No SRM) - If you like the idea of starting out with a really short run, this is perfect. \
It wont give you as much experience with stuff that applies to other categories, but it\'s still a \
great starting point. People usually recommend you start with the Kakariko route which gets the bottle normally, \
but you can start out with GIM if you are ambitious. A Kak route tutorial is in the resources channel.\n\n\
You can start with any of the other categories, these are just the most commonly suggested starting points. \
In the end you should run what you find most interesting. There are other non RTA options like Bingo as well.')

	@commands.command()
	async def cspointer(self, ctx):
		await ctx.send(
'Specific cutscenes will set a value which is very important for wrong warps called the “Cutscene Pointer”. \
In the context of an Any% Speedrun, this value is last set by the cutscene that plays when you enter the Deku Tree.\n\
If for whatever reason you need to reset the game after that cutscene, your CS Pointer gets set to the value for the title \
screen cutscene. Having this CS Pointer will mean that you will softlock after successfully performing the wrong warp.\n\
Luckily there is an easy way to fix this. Depending on your version, you can pause in a specific area to fix the relevant \
values. The fix is language and version specific. For the Japanese version:\n\
> 1.0 - pause the game in Link’s house\n\
> 1.1 - pause the game in House of Twins\n\
> 1.2 - pause the game in Link’s house\n\
After you have paused and unpaused the game in this location, the wrong warp will work again as long as your CS Pointer is \
still the title screen. \nA long explanation on the pause trick can be found here: <https://pastebin.com/WEkVWVWt>\n\
Also note: on the Practice ROM you can go to `warps > clear cs pointer` and it will make any wrong warp work regardless of your last cutscene.')

	@commands.command()
	async def dekuspeed(self, ctx):
		await ctx.send(
'The speed that Link will walk through doors with loading zones is dependant on how fast he entered the last loading zone. \
This is important for performing the Wrong Warp, because if Link doesn’t walk through the door at the right speed at the end of \
the setup, the warp timer value will not be correct.\n\n\
In a run context, the last loading zone before Gohma is entering The Deku Tree. This loading zone has a hard coded speed. No matter \
how fast or slow you enter it, it is the same. This means in runs you have nothing to worry about. However, in practice, if you warp to \
Gohmas room with the Practice ROM, chances are your warp speed is off and it will not work. You need to warp to Deku Tree *then* warp to \
Gohma for your loading zone speed value to be correct.')

	@commands.command()
	async def essadapter(self, ctx):
		await ctx.send(
'An ESS Adapter is a controller adapter that remaps the control stick for Wii Virtual Console. This makes the deadzone smaller, which makes \
angles feel more precise and ESS easier to hold like N64. It was originally created just to mimic the control stick mapping of N64, but \
other advanced features were added over time.\n\
Features include reversing the VC mapping, custom mapping options, \
pass-through mode, gamecube trigger mode, built-in input display, and modes for different games.\n\n\
Info: <https://electromodder.co.uk/>\n\
Buy: Sign up for the waitlist here to purchase: <https://electromodder.co.uk/waiting_list> \n\
Note: EM has support for a wider variety of VC titles, but that isn’t relevant for Ocarina of Time.')

	@commands.command()
	async def inputdisplay(self, ctx):
		await ctx.send(
'ESS adapters come with an input display, but if you are looking for a standalone option, DM HapticNoise on discord at Zach#7557 to inquire about purchasing one.')

	@commands.command()
	async def move(self, ctx):
		await ctx.send('You are in the wrong channel. Move to the correct one or Fig will be angry :rage:')

	@commands.command(aliases=['tutorial'])
	async def tutorials(self, ctx):
		await ctx.send(
'Arthur Oudini has many tutorials available for new players learning OoT speedrun tech.\n\
https://www.youtube.com/playlist?list=PLnMbZC1SexUfrFgCJ1EEOt0fL_Uc7FVRX')

	@commands.command()
	async def hess(self, ctx):
		await ctx.send(
'Check out this tutorial by Arthur Oudini for learning how to HESS.\n\
https://www.youtube.com/watch?v=5vRIpEKEuh4')

	@commands.command()
	async def superslide(self, ctx):
		await ctx.send(
'Check out this tutorial by Arthur Oudini for learning how to Superslide.\n\
https://www.youtube.com/watch?v=L2pI5sKut7k')

	@commands.command()
	async def megasidehop(self, ctx):
		await ctx.send(
'Check out this tutorial by Arthur Oudini for learning how to Mega Sidehop.\n\
https://www.youtube.com/watch?v=0IFT1C5q_RM')

	@commands.command()
	async def megaflip(self, ctx):
		await ctx.send(
'Check out this tutorial by Arthur Oudini for learning how to Mega Sidehop.\n\
https://www.youtube.com/watch?v=F4KDPo8lXA4')

	@commands.command()
	async def groundjump(self, ctx):
		await ctx.send(
'Check out this tutorial by Arthur Oudini for learning how to Ground Jump.\n\
https://www.youtube.com/watch?v=Q1rNKWf7nPA')

	@commands.command(aliases=['boatkeyskip'])
	async def boatskip(self, ctx):
		await ctx.send(
'Check out this tutorial by Arthur Oudini for learning how to Boat Skip with Chus/Nuts.\n\
https://www.youtube.com/watch?v=b-22kK1lOKY')

	@commands.command()
	async def ganondoor(self, ctx):
		await ctx.send(
'Check out this tutorial by Mikami for learning how to perform Ganondoor.\n\
https://www.youtube.com/watch?v=0AVFdMSPHPk')

	@commands.command()
	async def voidwarp(self, ctx):
		await ctx.send(
'Check out this video by sockfolder on child Void Warp. The description has more details as well explaining the setup.\n\
https://www.youtube.com/watch?v=2XGxgvXcN8g')

	@commands.command()
	async def instaclip(self, ctx):
		await ctx.send(
'Check out this tutorial by Zudu for learning how to Instaclip for Defeat Ganon No SRM.\n\
https://www.youtube.com/watch?v=AwjqKm58oKI')

	@commands.command(aliases=['reversebottleadventure'])
	async def rba(self, ctx):
		await ctx.send(
'Check out this video explaining RBA by dannyb.\n\
https://www.youtube.com/watch?v=lQQlbnJzxUI')

	@commands.command(aliases=['bottleadventure'])
	async def ba(self, ctx):
		await ctx.send(
'Check out this video explaining BA by dannyb.\n\
https://www.youtube.com/watch?v=a2rDwV9EwVo')

	@commands.command(aliases=['dot'])
	async def dotskip(self, ctx):
		await ctx.send(
'There\'s various ways to perform Door of Time Skip in Ocarina of Time. Depending on what you have \
available to you, you can pick the method you\'re most interested in. Lunge Storage is recommended for \
beginners as it\'s generally faster than pause buffering traditional dot skip.\n\n\
Traditional Sword/Swordless DoT Skip by Aliensqueakytoy:\n<https://www.youtube.com/watch?v=0BE2GYMD_6U>\n\
Lunge Storage by KeeganCG:\n<https://www.youtube.com/watch?v=GncyV4QuJCw>')

	@commands.command(aliases=['glitchexhibition','glitchshowcase'])
	async def glitches(self, ctx):
		await ctx.send(
'ZFG has a wonderful showcase featuring a large number of the glitches you can perform in OoT.\n\
https://www.youtube.com/watch?v=q2UnkvALVRs')

	@commands.command(aliases=['palwii'])
	async def palwii(self, ctx):
		await ctx.send(
'PAL systems natively run the game slower, even when using a region-free NTSC wad. \n\
You can solve this issue by using the WiiMod Lite homebrew and changing the video mode to NTSC.\n\
Link to the homebrew: <https://github.com/RiiConnect24/Wii-Mod-Lite/releases>')

def setup(bot):
	bot.add_cog(Faq(bot))
