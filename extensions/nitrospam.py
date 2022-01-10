import re
import discord
import asyncio
from discord.ext import commands

class SpamDetect(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.watchlist = {}

	@commands.Cog.listener('on_message')
	async def spam_detect(self, message):
		SPAM_COUNT = 3  # message count
		SPAM_TIME  = 10 # seconds buffer
		# ------------------------
		watchlist    = self.watchlist
		sender       = message.author
		channel      = message.channel
		server       = message.guild
		reporting_id = 304724247450877953
		reporting    = self.bot.get_channel(reporting_id)
		url          = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]\
		             |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)

		if url:
			# link detected in a message, add the user to a watch list
			# and keep track of the channels they've messaged with a link
			if sender not in watchlist:
				watchlist[sender] = {
					"count": 1,
					"channels": [channel],
					"messages": [message],
					"url": url[0]
				}
			# if the user is already being watched, check to see if the link
			# was posted in a new channel, if so, increase their watch count
			elif channel not in watchlist[sender]["channels"] and url[0] == watchlist[sender]["url"]:
					watchlist[sender]["count"] += 1
					watchlist[sender]["channels"].append(channel)
					watchlist[sender]["messages"].append(message)
			else:
				return

			# if the user has posted a SPAM_COUNT number of links all in 
			# different channels within a SPAM_TIME amount of time,
			# mark the user's messages for deletion
			if watchlist[sender]["count"] >= SPAM_COUNT:
				# grant the possible spammer role to mute them
				spammer_role = discord.utils.get(server.roles, name="Possible Spammer")
				await sender.add_roles(spammer_role)
				# report the incident to the mods channel
				await reporting.send(f"Possible spammer detected: {sender.mention}. Removed messages:")
				# relay the deleted messages to confirm it was spam, then delete them
				for message in watchlist[sender]["messages"]:
					await reporting.send(embed=discord.Embed(description=message.content))
					await message.delete()

			await asyncio.sleep(SPAM_TIME)

			# sanity check in case the user was removed from the
			# watchlist through some weird async race condition
			# (not sure how possible it is, just in case)
			if sender in watchlist:
				# lower watch level after spam timer runs out
				# and remove the sent channel from the list
				watchlist[sender]["count"] -= 1
				watchlist[sender]["channels"].remove(channel)
				if watchlist[sender]["count"] <= 0:
					del watchlist[sender]

def setup(bot):
	bot.add_cog(SpamDetect(bot))