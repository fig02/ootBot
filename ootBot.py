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

class OotBot(commands.Bot):
	async def setup_hook(self):
		await self.load_extension('extensions.roles')
		#await self.load_extension('extensions.twitch')
		await self.load_extension('extensions.faq')
		await self.load_extension('extensions.help')
		await self.load_extension('extensions.nitrospam')
		if config.get('Extra', 'enabled') == 'y':
			self.add_command(make_extra_command())
		synced = await self.tree.sync()
		print(f'synced {len(synced)} slash commands')
		config.create_update_timer()


# handling when the extra command is invoked
def make_extra_command():
	extra_command = config.get('Extra', 'command')
	extra_message = config.get('Extra', 'message')
	extra_error   = config.get('Extra', 'error')

	@commands.hybrid_command(name=extra_command, description='…')
	async def extra(ctx):
		await ctx.defer(ephemeral=True)
		# attempt to dm the user
		try:
			await ctx.author.send(content=extra_message, delete_after=30.0)
		except Forbidden:
			if ctx.interaction:
				await ctx.send(extra_error, ephemeral=True)
				return
			# let user know in public channel if dms are closed then delete after 10s
			error_msg = await ctx.send(extra_error)
			await asyncio.sleep(10)
			await ctx.message.delete()
			await error_msg.delete()
			return
		if ctx.interaction:
			await ctx.send('Check your DMs!', ephemeral=True)
			return
		# attempt to delete the command message that the user sent
		try:
			await ctx.message.delete()
		except Forbidden:
			# silently fail. command was likely sent via DM or bot doesn't have delete perms
			pass

	return extra

#create bot
intents = discord.Intents.default()
intents.message_content = False
client = OotBot(command_prefix = commands.when_mentioned, intents=intents)

#remove default help command
client.remove_command('help')

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

	if channel_id == strats_id and client.intents.message_content:
		if not url:
			if not media:
				embed=discord.Embed(color=sender.color, description=re.sub(r'@everyone|@here', '',message.content))
				embed.set_author(name=sender.display_name, icon_url=sender.display_avatar.url)
				await discussion.send(sender.mention + ' ' + strats.mention + ' is for videos only. Discussion should happen here instead.', embed=embed)
				await message.delete()
				return

		# valid media post, post about it in discussion for searching later
		embed=discord.Embed(color=sender.color, description=re.sub(r'@everyone|@here', '',re.sub(url_re, '', message.content).strip()))
		embed.set_author(name=sender.display_name, icon_url=sender.display_avatar.url)
		strat_url = media[0].url if media else url[0][0]
		embed.add_field(name="Link to video", value=strat_url, inline=False)
		embed.set_footer(text="New video posted!")
		bookmark = await discussion.send(embed=embed)

		# now make a link to the bookmark in the strats channel
		embed=discord.Embed(color=sender.color, title="View discussion for this video →", url=bookmark.jump_url)
		await strats.send(embed=embed)

#ready
@client.event
async def on_ready():
	print('ootBot is online')
	print('----------------')

#run
client.run(discord_token)
