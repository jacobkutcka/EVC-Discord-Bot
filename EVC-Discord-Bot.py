# General Imports
from os import system
from datetime import date
from time import sleep

# GPIO Imports
import RPi.GPIO as GPIO

# Discord Imports
import discord
from discord.ext import commands

# Discord section
TOKEN = <insert token here>
description = '''EVC Lab Bot'''
bot = commands.Bot(command_prefix='!', description=description)

# Set pin numbers to board mode
GPIO.setmode(GPIO.BOARD)

# Define button pins
closedbutton = #
pendingbutton = #
openbutton = #

# Button setup
GPIO.setup(closedbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pendingbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(openbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Event detection and callback
GPIO.add_event_detect(closedbutton, GPIO.BOTH, callback=closed, bounceime=800)
GPIO.add_event_detect(pendingbutton, GPIO.BOTH, callback=pending, bounceime=800)
GPIO.add_event_detect(openbutton, GPIO.BOTH, callback=open, bounceime=800)

# Function definition
def closed():
    print("BIG RED BUTTON")

def pending():
    print("Large Yellow Button")

def open():
    print("sizable green button")

while True:
    print("Waiting for button:")
