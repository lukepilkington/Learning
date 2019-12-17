#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Make an led blinking.
# auther      : www.freenove.com
# modification: 2018/08/02
########################################################################
import RPi.GPIO as GPIO
import time

ledRed = 11    # RPI Board pin11
ledYellow = 12 
buttonPin = 13

def setup():
	print ('Program is starting')
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(ledRed, GPIO.OUT)   # Set ledPin's mode is output
	GPIO.output(ledRed, GPIO.LOW)
	GPIO.setup(ledYellow, GPIO.OUT)   # Set ledPin's mode is output
	GPIO.output(ledYellow, GPIO.LOW)
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set ledPin low to off led
	print ('using pin%d'%ledRed)

def loop():
	while True:
		if GPIO.input(buttonPin)==GPIO.HIGH:
		
			GPIO.output(ledRed, GPIO.HIGH)  # led on
			print ('...red led on')
			time.sleep(1)
			
			GPIO.output(ledRed, GPIO.LOW) # led off
			print ('red led off...')
			time.sleep(1)
		
			GPIO.output(ledYellow,GPIO.HIGH)
			print ('....yellow led on')
			time.sleep(1)
		
			GPIO.output(ledYellow,GPIO.LOW)
			print ('yellow led off...')
			time.sleep(1)
		
		else: 
			GPIO.output(ledYellow,GPIO.LOW)
			print ('yellow led off...')
			GPIO.output(ledRed, GPIO.LOW) # led off
			print ('red led off...')
		
	
def destroy():
	GPIO.output(ledRed, GPIO.LOW) 
	GPIO.output(ledYellow, GPIO.LOW)    # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

