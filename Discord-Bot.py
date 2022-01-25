from os import system
from datetime import date
from time import sleep

from gpiozero import LED, Button
import discord
from discord.ext import commands

import asyncio

# Pull in server token and channel ID
with open('token.txt', 'r') as f:
	TOKEN = f.read()
with open('channel.txt', 'r') as f:
	CHANNEL = f.read()

# Define bot properties
description = '''EVC Lab Bot'''
bot = commands.Bot(command_prefix='!', description=description)

# Define client
client = discord.Client()

# Button and LED GPIO pins
openbutton=Button(17)
pendingbutton=Button(27)
closedbutton=Button(22)
###
openlight=LED(4)
pendinglight=LED(23)
closedlight=LED(24)

# Saved Messages
openmessage=':green_circle: :radio_button: :radio_button: OPEN :green_circle: :radio_button: :radio_button:'
pendingmessage=':radio_button: :yellow_circle: :radio_button: PENDING :radio_button: :yellow_circle: :radio_button:'
closedmessage=':radio_button: :radio_button: :red_circle: CLOSED :radio_button: :radio_button: :red_circle:'

print('Program Initialized')

@bot.event
async def msg(status):
	channel = bot.get_channel(int(CHANNEL))
	print('Bot channel: ' + str(channel))
	print('Channel int: ' + str(CHANNEL))
	print('Sending message...')
	if status == 'open':
		await channel.send(openmessage)
	elif status == 'pending':
		await channel.send(pendingmessage)
	elif status == 'closed':
		await channel.send(closedmessage)
	print('Finished.')

@bot.event
async def on_ready():
	# Tell me on_ready() def has started
	print('On ready!')
	# Endless while loop
	while True:
		# Open status
		if openbutton.is_pressed:
			print('Green Button Pressed')
			await msg('open')
			openlight.on()
			pendinglight.off()
			closedlight.off()
			openbutton.wait_for_release()
		# Pending status
		elif pendingbutton.is_pressed:
			print('Yellow Button Pressed')
			await msg('pending')
			openlight.off()
			pendinglight.on()
			closedlight.off()
			pendingbutton.wait_for_release()
		# Closed status
		elif closedbutton.is_pressed:
			print('Red Button Pressed')
			await msg('closed')
			openlight.off()
			pendinglight.off()
			closedlight.on()
			closedbutton.wait_for_release()

# Start bot
bot.run(TOKEN)
# Tell me the bot booted
print('Bot is booted')

