######################################################################
# Drive both right wheels and check right wheel encoder data
import RPi.GPIO as gpio
import time
import numpy as np

###### Initialize GPIO pins #######

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(31, gpio.OUT)  # IN1
	gpio.setup(33, gpio.OUT)  # IN2
	gpio.setup(35, gpio.OUT)  # IN3
	gpio.setup(37, gpio.OUT)  # IN4
	gpio.setup(12, gpio.IN, pull_up_down = gpio.PUD_UP)

def gameover():
	gpio.output(31,  False)
	gpio.output(33,  False)
	gpio.output(35,  False)
	gpio.output(37,  False)
	gpio.cleanup()


######## Main Code ########
init()

counter = np.uint64(0)
button = int(0)

# Initialize pwm signal to control motor
pwm = gpio.PWM(37, 100)
val = 30
pwm.start(val)
time.sleep(0.1)

while(True):
	print("Counter =", counter, "GPIO state: ", gpio.input(12))
	if int(gpio.input(12)) != int(button):
		button = int(gpio.input(12))
		counter += 1

	if counter >= 960:
		pwm.stop()
		gameover()
		print("Thanks for playing")
		break
