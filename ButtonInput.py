#from os import system
from datetime import date
from time import sleep

from gpiozero import LED, Button

openbutton=Button(17)
pendingbutton=Button(27)
closedbutton=Button(22)

openlight= LED(4)
pendinglight= LED(23)
closedlight=LED(24)

print('Waiting for Button')

while True:
	if closedbutton.is_pressed:
		print('BIG RED BUTTON')
		openlight.off()
		pendinglight.off()
		closedlight.on()
		closedbutton.wait_for_release()
	elif pendingbutton.is_pressed:
		print('Large Yellow Button')
		openlight.off()
		pendinglight.on()
		closedlight.off()
		pendingbutton.wait_for_release()
	elif openbutton.is_pressed:
		print('sizable green button')
		openlight.on()
		pendinglight.off()
		closedlight.off()
		openbutton.wait_for_release()
GPIO.cleanup()
