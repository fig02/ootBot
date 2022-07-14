#! /bin/env python3

import re
import discord
import asyncio
import sys
from discord import Forbidden
from discord.ext import commands
from updater import BotConfig

config = BotConfig()

discord_token = config.get('Bot Settings', 'discord_token')

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
	strats_id     = int(config.get('Server Settings', 'strats_id'))
	discussion_id = int(config.get('Server Settings', 'discussion_id'))
	strats        = client.get_channel(strats_id)
	discussion    = client.get_channel(discussion_id)
	url_re        = r'((http|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]))'
	url           = re.findall(url_re, message.content)

	# handling text posted in the strats channel
	if sender.id == client.user.id:
		# bail if post is from the bot itself
		return

	if channel_id == strats_id:
		if not url:
			if not media:
				embed=discord.Embed(color=sender.color, description=re.sub(r'@everyone|@here', '',message.content))
				embed.set_author(name=sender.display_name, icon_url=sender.avatar_url)
				await discussion.send(sender.mention + ' ' + strats.mention + ' is for videos only. Discussion should happen here instead.', embed=embed)
				await message.delete()
				return

		# valid media post, post about it in discussion for searching later
		embed=discord.Embed(color=sender.color, description=re.sub(r'@everyone|@here', '',re.sub(url_re, '', message.content).strip()))
		embed.set_author(name=sender.display_name, icon_url=sender.avatar_url)
		strat_url = media[0].url if media else url[0][0]
		embed.add_field(name="Link to video", value=strat_url, inline=False)
		embed.set_footer(text="New video posted!")
		bookmark = await discussion.send(embed=embed)

		# now make a link to the bookmark in the strats channel
		embed=discord.Embed(color=sender.color, title="View discussion for this video →", url=bookmark.jump_url)
		await strats.send(embed=embed)

	# handling when the extra command is invoked
	if config.get('Extra', 'enabled') == 'y':
		extra_prefix  = await client.get_prefix(message)
		extra_command = config.get('Extra', 'command')
		extra_message = config.get('Extra', 'message')
		extra_error   = config.get('Extra', 'error')
		if type(extra_prefix) is list:
			extra_prefix = extra_prefix[0]
		if message.content.startswith(f'{extra_prefix}{extra_command}'):
			# attempt to dm the user
			try:
				await sender.send(content=extra_message, delete_after=30.0)
			except Forbidden:
				# let user know in public channel if dms are closed then delete after 10s
				error_msg = await message.channel.send(extra_error)
				await asyncio.sleep(10)
				await message.delete()
				await error_msg.delete()
				return
			# attempt to delete the command message that the user sent
			try:
				await message.delete()
			except Forbidden:
				# silently fail. command was likely sent via DM or bot doesn't have delete perms
				pass
			return

#ready
@client.event
async def on_ready():
	print('ootBot is online')
	print('----------------')

#update
config.create_update_timer(client)

#run
client.run(discord_token)