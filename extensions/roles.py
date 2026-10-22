import discord
from discord import app_commands
from discord.ext import commands

role_options = ['any', 'gsr', 'mst', 'ad', 'hundo',
			   'glitchless', 'noww','bingo', 'extensions', 
			   'mq', 'gdq', 'defeat-ganon', 'nocturne-rta']

class Roles(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	async def missing_roles(self, ctx, names):
		missing = [name for name in names if not discord.utils.get(ctx.guild.roles, name=name)]
		if missing:
			await ctx.send(ctx.author.mention + ' Role does not exist: `' + '`, `'.join(missing) + '`')
		return missing

	def suggest_roles(self, current, options):
		words = current.lower().split()
		if current.endswith(' ') or not words:
			done, partial = words, ''
		else:
			done, partial = words[:-1], words[-1]
		prefix = ' '.join(done) + (' ' if done else '')
		return [
			app_commands.Choice(name=prefix + role, value=prefix + role)
			for role in options
			if role.startswith(partial) and role not in done
		][:25]

	@commands.hybrid_command(description='add one or more roles seperated by spaces')
	@app_commands.describe(roles='roles to add, seperated by spaces (see /roles)')
	async def add(self, ctx, *, roles: str):
		await ctx.defer()
		args = [element.lower() for element in roles.split()] #force args to lowercase
		user = ctx.author
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

		if is_valid and await self.missing_roles(ctx, ['Ocarina of Time'] + args):
			return

		#if roles are valid, give oot role/add desired roles/generate and send response
		if is_valid:
			await user.add_roles(discord.utils.get(user.guild.roles, name='Ocarina of Time'))
			for i in args:
				await user.add_roles(discord.utils.get(user.guild.roles, name=i))
				response += '> ' + i + '\n'
			await ctx.send(response)

	@commands.hybrid_command(description='remove one or more roles seperated by spaces')
	@app_commands.describe(roles='roles to remove, seperated by spaces (see /roles)')
	async def remove(self, ctx, *, roles: str):
		await ctx.defer()
		args = [element.lower() for element in roles.split()] #force args to lowercase
		user = ctx.author
		is_valid = 1 #roles are valid flag
		response = user.mention + ' has been removed from the following roles:\n'

		#check for valid roles
		for i in args:
			if i not in role_options:
				#invalid role detected
				await ctx.send(user.mention + " `" + i + '` is not a valid role. Please correct and re-send your request.')
				is_valid = 0
				break

		if is_valid and await self.missing_roles(ctx, args):
			return

		#if roles are valid, remove roles + generate and send response
		if is_valid:
			for i in args:
				await user.remove_roles(discord.utils.get(user.guild.roles, name=i))
				response += '> ' + i + '\n'
			await ctx.send(response)

	@commands.hybrid_command(description='list available roles')
	async def roles(self, ctx):
		await ctx.send('''
```
any           - Any%
gsr           - Ganondorf Source Requirement
mst           - Medallions, Stones, Trials
ad            - All Dungeons
hundo         - 100%
glitchless    - Glitchless
defeat-ganon  - Defeat Ganon
noww          - No Wrong Warp
bingo         - Bingo
extensions    - Category Extensions
mq            - Master Quest
```
		''')

	@add.autocomplete('roles')
	async def add_autocomplete(self, interaction, current):
		return self.suggest_roles(current, role_options)

	@remove.autocomplete('roles')
	async def remove_autocomplete(self, interaction, current):
		owned = [role.name for role in interaction.user.roles]
		return self.suggest_roles(current, [role for role in role_options if role in owned])

async def setup(bot):
	await bot.add_cog(Roles(bot))
