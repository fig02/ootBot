import sys
import os.path

import subprocess

import asyncio

import yaml

CONFIG_FILE = 'config.yml'

class BotConfig:
	def __init__(self):
		self.update_task = None
		if not os.path.exists(CONFIG_FILE):
			# no config available
			print(f'{CONFIG_FILE} not found. Copy config-template.yml to {CONFIG_FILE} and fill it in.')
			sys.exit(1)
		with open(CONFIG_FILE) as f: self.config = yaml.safe_load(f)
		self.print()

	def __getitem__(self, key):
		return self.config[key]

	def print(self):
		print("----------------")
		print("|    config    |")
		print("----------------")
		print(yaml.safe_dump(self._redacted(self.config), sort_keys=False, allow_unicode=True))

	def _redacted(self, value):
		if not isinstance(value, dict):
			return value
		redacted = {}
		for k, v in value.items():
			if k == 'discord_token':
				# don't print the discord token lol
				v = f'{v[:12]}...'
			elif k == 'message':
				# the extra command's message can contain passwords
				v = '<hidden>'
			else:
				v = self._redacted(v)
			redacted[k] = v
		return redacted

	def create_update_timer(self):
		if self['auto_update']:
			self.update_task = asyncio.create_task(self.timer())

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
