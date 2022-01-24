from os import system
from datetime import date
from time import sleep

from gpiozero import LED, Button
import discord
from discord.ext import commands

with open('token.txt', 'r') as f:
	TOKEN = f.read()
with open('channel.txt', 'r') as f:
	CHANNEL = f.read()
description = '''EVC Lab Bot'''
bot = commands.Bot(command_prefix='!', description=description)

client = discord.Client()

openbutton=Button(17)
pendingbutton=Button(27)
closedbutton=Button(22)

openlight=LED(4)
pendinglight=LED(23)
closedlight=LED(24)

openmessage=':green_circle: :radio_button: :radio_button: OPEN :green_circle: :radio_button: :radio_button:'
pendingmessage=':radio_button: :yellow_circle: :radio_button: PENDING :radio_button: :yellow_circle: :radio_button:'
closedmessage=':radio_button: :radio_button: :red_circle: CLOSED :radio_button: :radio_button: :red_circle:'

@client.event
async def msg(status):
	await ctrx.send('shit works')


def on_ready():
	print('on ready')
	while True:
		if openbutton.is_pressed:
			print('sizable green button')
			msg('open')
			openlight.on()
			pendinglight.off()
			closedlight.off()
			openbutton.wait_for_release()
			sleep(10)
		elif pendingbutton.is_pressed:
			print('Large Yellow Button')
			
			openlight.off()
			pendinglight.on()
			closedlight.off()
			pendingbutton.wait_for_release()
			sleep(10)
		elif closedbutton.is_pressed:
			print('BIG RED BUTTON')
			
			openlight.off()
			pendinglight.off()
			closedlight.on()
			closedlight.wait_for_release()
			sleep(10)

bot.run(TOKEN)
print('booting')
on_ready()
