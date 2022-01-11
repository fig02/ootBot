import re
import discord
from discord.ext import commands

discord_token = ''

#create bot
client = commands.Bot(command_prefix = '!')

#remove default help command
client.remove_command('help')

#load custom extensions
client.load_extension('extensions.roles')
#client.load_extension('extensions.twitch')
client.load_extension('extensions.faq')
client.load_extension('extensions.help')
client.load_extension('extensions.nitrospam')

#strats-and-setups link detection
@client.event
async def on_message(message):
	await client.process_commands(message) #handle commands

	channel_id    = message.channel.id
	media         = message.attachments
	sender        = message.author
	strats_id     = 357309453311148032
	discussion_id = 495387041161543690
	strats        = client.get_channel(strats_id)
	discussion    = client.get_channel(discussion_id)
	url           = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]\
		          |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)

	if channel_id == strats_id:
		if not url:
			if not media:
				embed=discord.Embed(color=sender.color, description=re.sub(r'@everyone|@here', '',message.content))
				embed.set_author(name=sender.display_name, icon_url=sender.avatar_url)
				await discussion.send(sender.mention + ' ' + strats.mention + ' is for videos only. Discussion should happen here instead.', embed=embed)
				await message.delete()

#ready
@client.event
async def on_ready():
	print('ootBot is online')
	print('----------------')

#run
client.run(discord_token)
