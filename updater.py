import configparser
import sys
import os.path

import subprocess

import asyncio

class BotConfig:
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.config.read('config.txt')
		if not self.config.sections():
			# no config available
			self.create_default()
		self.print()

	def get(self, section, key):
		return self.config[section][key]

	def create_default(self):
		# make a new config
		self.config = configparser.ConfigParser()
		self.config['Server Settings'] = {
			'strats_id': 357309453311148032,
			'discussion_id': 495387041161543690
		}
		self.config['Bot Settings'] = {
			'discord_token': 'REPLACE_WITH_YOUR_DISCORD_TOKEN'
		}
		self.config['GitHub'] = {
			'is_repo': 'n'
		}
		with open('config.txt', 'w') as f: self.config.write(f)
		self.set()

	def set(self):
		for section in self.config:
			if section == "DEFAULT": continue
			print(f'[{section}]')
			for key in self.config[section]:
				value = input(f'{key}? ({self.config[section][key]}):')
				if value: 
					self.config[section][key] = value
		with open('config.txt', 'w') as f: self.config.write(f)

	def print(self):
		print("----------------")
		print("|    config    |")
		print("----------------")
		# print out each non default section of config
		for section in self.config:
			if section == "DEFAULT": continue
			print(f'[{section}]')
			for key in self.config[section]:
				value = self.config[section][key]
				# don't print the discord token lol
				if key == 'discord_token':
					value = f'{value[:12]}...'
				print(f'{key} = {value}')
			print('')

	def create_update_timer(self, bot):
		if (self.get('GitHub', 'is_repo') == 'y'):
			bot.loop.create_task(self.timer())

	async def timer(self):
		while True:
			await asyncio.sleep(60)
			subprocess.check_output(["git", "fetch"])
			output = subprocess.check_output(["git", "status"])
			output = output.decode("utf-8")
			if 'Your branch is behind' not in output:
				continue
			print("Update detected, pulling and exiting...")
			output = subprocess.check_output(["git", "pull"])
			output = output.decode("utf-8")
			print(output)
			sys.exit(0) 