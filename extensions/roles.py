import discord
from discord.ext import commands

role_options = ['any', 'gsr', 'mst', 'ad', 'hundo',
			   'glitchless', 'ganonless', 'noww',
			   'bingo', 'extensions', 'mq', 'gdq']

class Roles(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def add(self, ctx, *args):
		args = [element.lower() for element in args] #force args to lowercase
		user = ctx.message.author
		is_valid = 1 #roles are valid flag
		response = user.mention + ' has been assigned the following roles:\n'

		#check for valid roles
		for i in args:
			if i not in role_options:
				#tell user that oot role is added automatically
				if i == 'oot' or i == 'ocarina':
					await ctx.send(user.mention + ' The `Ocarina of Time` role is added automatically when a category role is assigned.')
					is_valid = 0
					break
				#invalid role detected
				await ctx.send(user.mention + " `" + i + '` is not a valid role. Please correct and re-send your request.')
				is_valid = 0
				break

		#if roles are valid, give oot role/add desired roles/generate and send response
		if is_valid:
			#await user.add_roles(discord.utils.get(user.guild.roles, name='Ocarina of Time'))
			for i in args:
				await user.add_roles(discord.utils.get(user.guild.roles, name=i))
				response += '> ' + i + '\n'
				if i == 'gdq':
					response += 'The gdq role is a temporary role used for organizing oot related things at the event.'
			await ctx.send(response)

	@commands.command()
	async def remove(self, ctx, *args):
		args = [element.lower() for element in args] #force args to lowercase
		user = ctx.message.author
		is_valid = 1 #roles are valid flag
		response = user.mention + ' has been removed from the following roles:\n'

		#check for valid roles
		for i in args:
			if i not in role_options:
				#invalid role detected
				await ctx.send(user.mention + " `" + i + '` is not a valid role. Please correct and re-send your request.')
				is_valid = 0
				break

		#if roles are valid, remove roles + generate and send response
		if is_valid:
			for i in args:
				await user.remove_roles(discord.utils.get(user.guild.roles, name=i))
				response += '> ' + i + '\n'
			await ctx.send(response)

	@commands.command()
	async def roles(self, ctx):
		await ctx.send('''
```
any        - Any%
gsr        - Ganondorf Source Requirement
mst        - Medallions, Stones, Trials
ad         - All Dungeons
hundo      - 100%
glitchless - Glitchless
ganonless  - Ganonless
noww       - No Wrong Warp
bingo      - Bingo
extensions - Category Extensions
mq         - Master Quest
```
		''')

def setup(bot):
	bot.add_cog(Roles(bot))
