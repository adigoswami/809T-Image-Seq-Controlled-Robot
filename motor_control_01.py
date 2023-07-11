# Functions defiend for moving left, right, forward and backwards

import RPi.GPIO as gpio
import time

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(31, gpio.OUT) # IN1
	gpio.setup(33, gpio.OUT) # IN2
	gpio.setup(35, gpio.OUT) # IN3
	gpio.setup(37, gpio.OUT) # IN4
	gpio.setup(16, gpio.OUT) # trig
	gpio.setup(18, gpio.IN)  # Echo
	gpio.setup(36, gpio.OUT) # Servo

def gameover():
	# Set all pins low
	gpio.output(31, False)
	gpio.output(33, False)
	gpio.output(35, False)
	gpio.output(37, False)

def forward(tf):
	#init()
	# Left wheels
	gpio.output(31, True) # Left Forward
	gpio.output(33, False) # Left Backward
	
	# Right wheels
	gpio.output(35, False) # Right Backward
	gpio.output(37, True) # Right Forward

	# Wait
	time.sleep(tf)
	gameover()
	#gpio.cleanup()

def reverse(tf):
	#init()
	# Left wheels
	gpio.output(31, False) # Left Forward
	gpio.output(33, True) # Left Backward
	
	# Right wheels
	gpio.output(35, True) # Right Backward
	gpio.output(37, False) # Right Forward

	# Wait
	time.sleep(tf)
	gameover()
	#gpio.cleanup()

def pivotleft(tf):
	#init()
	# Left wheels
	gpio.output(31, False) # Left Forward
	gpio.output(33, True) # Left Backward
	
	# Right wheels
	gpio.output(35, False) # Right Backward
	gpio.output(37, True) # Right Forward

	# Wait
	time.sleep(tf)
	gameover()
	#gpio.cleanup()

def pivotright(tf):
	#init()
	# Left wheels
	gpio.output(31, True) # Left Forward
	gpio.output(33, False) # Left Backward
	
	# Right wheels
	gpio.output(35, True) # Right Backward
	gpio.output(37, False) # Right Forward

	# Wait
	time.sleep(tf)
	gameover()
	#gpio.cleanup()
