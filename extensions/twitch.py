import discord
from discord.ext import tasks, commands
from twitch import TwitchHelix

twitch_token  = ''
helix = TwitchHelix(client_id=twitch_token)
oot = 11557
streams_id = 624584018549145621

whitelist = ['any%', '100%', 'hundo', 'mst', 'ad', 'dungeons',
			 'gsr', 'requirement', 'glitchless', 'restricted', 
			 'unrestricted', 'ganonless', 'warp', 'bingo', 'snb',
			 'esnb', 'mq', 'faster', 'speedrun', 'speedruns', 'tas',
			 'tasing', 'research', 'timing', 'route', 'practice',
			 'ww', 'im/ww', 'nsr', 'puzzle', 'science']

blacklist = ['randomizer', 'randomiser', 'ootr', 'zootr', 'rando', 'ootrandomizer', 'casual', 'weekly',
			 'sanity', 'keysanity', 'allsanity', 'tokensanity', 'lets', 'let\'s',
			 '3d', '3ds', 'hunt', 'mw', 'accessible', 'seed', 'co-op']

class Twitch(commands.Cog):
	def __init__(self, bot, timer, active_streams):
		self.bot = bot
		self.twitch.start()
		self.timer = timer
		self.active_streams = active_streams

	@tasks.loop(minutes=5.0)
	async def twitch(self):
		streams_channel = self.bot.get_channel(streams_id)
		request = helix.get_streams(game_ids=[oot])
		oot_streams = request

		#create user/title pairs
		user_title = {}
		streams = {}
		for i in oot_streams:
			streams.update({i['user_name']:i['title']})
			user_title.update({i['user_name']:i['title'].split(' ')})

		#make stream title a list of words and make them lowercase
		title_lower = {}
		for i in user_title:
			title = user_title[i]
			title = [word.lower() for word in title]
			title_lower.update({i:title})

		#compare words in stream title with whitelist and add to new dict
		whitelisted_streams = {}
		for i in title_lower:
			for word in title_lower[i]:
				if (word in whitelist):
					whitelisted_streams.update({i:title_lower[i]})

		#compare words in stream title and add valid streamers to a new list
		valid_streams = []
		for i in whitelisted_streams:
			valid = True
			for word in whitelisted_streams[i]:
				if word in blacklist:
					valid = False
					break
			if valid:
				valid_streams.append(i)

		#find streams that werent posted last update
		new_streams = []
		for i in valid_streams:
			if i not in self.active_streams:
				new_streams.append(i)

		#remove streams from active_streams that went offline
		for i in self.active_streams:
			if i not in valid_streams:
				self.active_streams.remove(i)

		#add the new streams to active_streams
		for i in new_streams:
			self.active_streams.append(i)

		#post new streams
		for i in streams:
			for j in new_streams:
				if i == j:
					name_lower = i.lower()
					embed = discord.Embed(title=streams[i], description="https://www.twitch.tv/%s" % (name_lower),colour=0x6441A4)
					embed.set_author(name=i + ' is now live on Twitch!')
					embed.set_thumbnail(url='https://www.twitch.tv/p/assets/uploads/glitch_474x356.png')
					if timer > 0:
						await streams_channel.send(content=None, embed=embed)

		print(self.timer)
		self.timer += 5

	@twitch.before_loop
	async def before_twitch(self):
		await self.bot.wait_until_ready()

def setup(bot):
	bot.add_cog(Twitch(bot, 0, []))