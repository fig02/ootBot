import discord
import asyncio
from discord.ext import commands

class SpamDetect(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.watchlist = {}

	def is_user_message(self, message):
		return (
			message.guild is not None
			and not message.author.bot
			and message.type in (discord.MessageType.default, discord.MessageType.reply)
		)

	@commands.Cog.listener('on_message')
	async def spam_detect(self, message):
		SPAM_COUNT = 3  # message count
		SPAM_TIME  = 32 # seconds buffer
		# ------------------------
		watchlist    = self.watchlist
		sender       = message.author
		channel      = message.channel
		server       = message.guild
		reporting_id = 930478562652332082
		reporting    = self.bot.get_channel(reporting_id)

		if not self.is_user_message(message):
			return

		if sender not in watchlist:
			# add the user to the watchlist and track this message.
			watchlist[sender] = {
				"count": 1,
				"channels": [channel],
				"messages": [message]
			}
		# if the user is being watched, check if they posted again.
		else:
			watchlist[sender]["messages"].append(message)
			if channel in watchlist[sender]["channels"]:
				if watchlist[sender]["count"] >= SPAM_COUNT:
					try:
						await message.delete()
					except discord.NotFound:
						pass
				return
			watchlist[sender]["count"] += 1
			watchlist[sender]["channels"].append(channel)

		# if the user has posted a message in SPAM_COUNT different channels
		# within a SPAM_TIME window, treat it as spam.
		if watchlist[sender]["count"] >= SPAM_COUNT:
			# grant the possible spammer role to mute them.
			spammer_role = discord.utils.get(server.roles, name="Possible Spammer")
			await sender.add_roles(spammer_role)
			try:
				# report the incident to the mods channel.
				if reporting:
					channels = ", ".join(c.mention for c in watchlist[sender]["channels"])
					await reporting.send(
						f"Possible spammer detected: {sender.mention}. "
						f"Removed messages in {watchlist[sender]['count']} channels: {channels}"
					)
				else:
					print(f"nitrospam: reporting channel {reporting_id} not found, check reporting_id in nitrospam.py")
			finally:
				# delete the spam messages.
				for msg in watchlist[sender]["messages"]:
					try:
						await msg.delete()
					except discord.NotFound:
						pass

		await asyncio.sleep(SPAM_TIME)

		# sanity check in case the user was removed from the
		# watchlist through some weird async race condition
		# (not sure how possible it is, just in case).
		if sender in watchlist:
			# lower watch level after spam timer runs out
			# and remove the sent channel from the list.
			watchlist[sender]["count"] -= 1
			watchlist[sender]["channels"].remove(channel)
			if watchlist[sender]["count"] <= 0:
				del watchlist[sender]

async def setup(bot):
	await bot.add_cog(SpamDetect(bot))
