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
or right click on the game in you games list to change settings.\n\
Guide: <https://imgur.com/a/bCdVV>')

	@commands.command()
	async def watches(self, ctx):
		await ctx.send(
'To see values from RAM in the Practice ROM, you need to use the Watches menu.\n\
Address and flags list: <https://bthl.es/0f>')

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
Any% - If you like the idea of starting out with a really short run, this is perfect. It wont give you as \
much experience with stuff that applies to other categories, but it\'s still a great starting point. \
People usually recommend you start with the Kakariko route which gets the bottle normally, but you can \
start out with GIM if you are ambitious. A Kak route tutorial is in the resources channel.\n\n\
GSR - This category is very commonly recommended to beginners. It involves completing Shadow, Spirit, \
and doing most of Forest before beating the game. The category will teach you lots of fundamentals that will carry over to more \
advanced categories. A common downside cited about this category is mainly the amount of cutscenes you \
have to sit through. There is a tutorial in the resources section. Note that some parts are out of date, \
especially the “Boat Skip” trick.\n\n\
Glitchless - This category is great to start with because it focuses more on movement than anything else. \
This lays the groundwork for being fast at other categories. A 4 hour run is pretty long for beginners, but \
if you are okay with the length, this is another great starting point. For obvious reasons, this category \
has a lot of cutscenes too. Join the glitchless discord for more help centered around specifically glitchless. \n\n\
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
	async def consoles(self, ctx):
		await ctx.send(
'There are many options in terms of consoles for running this game. Here is some info about all of them:\n\
N64 - This console has the advantage of being able to run all 3 versions of the game. However it suffers from more lag and slower loading \
speeds. Having access to version exclusive glitches makes it faster in some cases. Currently that includes the All Dungeons category, \
GSR (by probably only a small amount) and Ganonless.\n\n\
Wii VC - This is the most common version you will see OoT ran on. This version only has access to the 1.2 version, but has many \
exclusive glitches that are unique to the emulator itself. Wii VC also has much less lag and faster loads than N64. Other than the \
main categories mentioned above, you will see that Wii VC is faster for everything else. It suffers from a poor control stick mapping, \
but that can be fixed by an ESS Adapter.\n\n\
WiiU VC - While this console technically has faster loads and less lag than Wii VC, the control stick mapping and pause buffering \
differences make it much less enjoyable to play on. It also has significantly more input delay than any other console. WiiU does not \
have some of the exclusive glitches that Wii does. For example, the Any% GIM does not work with sticks/nuts, and stick as adult will crash \
in some places which is important for 100%\n\n\
iQue - iQue was used a while back for being the fastest for Any%, but that hasn’t been the case for a long time. It is not great in terms of version \
exclusive glitches since it\'s 1.2 without the VC specific emulator glitches. This console has really fast chinese text so it is technically \
fast for Glitchless, and possibly GSR. But due to its poor accessibility and terrible controls, no one chooses to use it.\n\n\
Emulator (PC) - Project 64 versions 1.6 and 1.7 are the only emulators allowed for this game. Due to it being an unofficial emulator, emu \
runs are only allowed until the top 10% of runs per category. To get this number, multiply the current record of a given category by 0.1.')

	@commands.command()
	async def essadapter(self, ctx):
		await ctx.send(
'An ESS Adapter is a controller adapter that remaps the control stick for Wii Virtual Console.This makes the deadzone smaller, which makes \
angles feel more precise and ESS easier to hold like N64. It was originally created just to mimic the control stick mapping of N64, but \
other advanced features were added over time.\n\
Currently there are two main options for buying an adapter. Both have similar features like reversing the VC mapping, custom mapping options, \
pass-through mode, gamecube trigger mode, built-in input display, and modes for different games.\n\n\
Electromodder:\n\
Info: <https://electromodder.co.uk/>\n\
Buy: Sign up for the waitlist here to purchase: <https://electromodder.co.uk/waiting_list> \n\
Note: EM has support for a wider variety of VC titles, but that isn’t relevant for Ocarina of Time. His is the only current option for Classic Controller.\n\n\
Zas:\n\
Info: <https://essadapter.com/> \n\
Buy: DM him on discord at Zas#8567 \n\n\
If you plan to make your own adapter, make sure it conforms to these guidelines: <https://pastebin.com/0yXeqQZx>')

	@commands.command()
	async def inputdisplay(self, ctx):
		await ctx.send(
'ESS adapters come with an input display, but if you are looking for a standalone option, DM HapticNoise on discord at Zach#7557 to inquire about purchasing one.')

	@commands.command()
	async def move(self, ctx):
		await ctx.send('You are in the wrong channel. Move to the correct one or Fig will be angry :rage:')

def setup(bot):
	bot.add_cog(Faq(bot))
