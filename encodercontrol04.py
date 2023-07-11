#################################################################
##### Drive all motors and see their encoders values

import RPi.GPIO as gpio
import time
import numpy as np

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(31, gpio.OUT) # IN1
	gpio.setup(33, gpio.OUT) # IN2
	gpio.setup(35, gpio.OUT) # IN3
	gpio.setup(37, gpio.OUT) # IN4

	gpio.setup(7, gpio.IN, pull_up_down = gpio.PUD_UP)
	gpio.setup(12, gpio.IN, pull_up_down = gpio.PUD_UP)

def gameover():
	gpio.output(31, False)
	gpio.output(33, False)
	gpio.output(35, False)
	gpio.output(37, False)
	gpio.cleanup()

####### Main Code ########
init()
counterFL = np.uint64(0)
counterBR = np.uint64(0)

buttonBR = int(0)
buttonFL = int(0)

# Independent motor control via pwm
pwm1 = gpio.PWM(31, 50) # BackRight motor
pwm2 = gpio.PWM(37, 50) # FrontLeft motor
val = 22
pwm1.start(val)
pwm2.start(val)
time.sleep(0.1)

while(True):

	print("CounterBR:", counterBR, "CounterFL:", counterFL, "BR state:", gpio.input(12), "FL state:", gpio.input(7))
	if int(gpio.input(12)) != int(buttonBR):
		buttonBR = int(gpio.input(12))
		counterBR += 1

	if int(gpio.input(7)) != int(buttonFL):
		buttonFL = int(gpio.input(7))
		counterFL += 1

	if counterFL >= 960:
		pwm1.stop()

	if counterBR >= 960:
		pwm2.stop()

	if counterBR >= 960 and counterFL >= 960:
		gameover()
		break

