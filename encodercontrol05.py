import RPi.GPIO as gpio
import time
import math
import numpy as np
from simple_pid import PID

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

##############################################################
################### Main Code ################################
init()
counterFL = np.uint64(0)
counterBR = np.uint64(0)

buttonFL = int(0)
buttonBR = int(0)

mode = input("Enter mode 'w', 's', 'd', 'a': ")

if mode == 'w':
	pwm1 = gpio.PWM(31, 100) # Left Forward
	pwm2 = gpio.PWM(37, 100) # Right Forward
elif mode == 's':
	pwm1 = gpio.PWM(33, 100) # Left Backward
	pwm2 = gpio.PWM(35, 100) # Right Backward
elif mode == 'd':
	pwm1 = gpio.PWM(31, 100) # Left Forward
	pwm2 = gpio.PWM(35, 100) # Right Backward
elif mode == 'a':
	pwm1 = gpio.PWM(33, 100) # Left Backward
	pwm2 = gpio.PWM(37, 100) # Right Forward

if mode == 'w' or mode == 's':
	distance = float(input("Enter distance in meters: "))
	target = int((distance*1000*960)/(65*math.pi))
elif mode == 'a' or mode == 'd':
	angle = float(input("Enter angle in degrees: "))
	distance = (math.pi * 250 * angle)/360
	target = int((distance * 960)/(65 * math.pi)) 

time.sleep(5)

if mode == 'w' or mode == 's':
	pwm1.start(25) # Change Please
	pwm2.start(25)

	time.sleep(0.1)

	pid = PID(0.001, 10, 0.1, setpoint = 0)

	pid.output_limits = (0, 35)

	start_time = 0

else:
	pwm1.start(50) # Change Please
	pwm2.start(50)

	time.sleep(0.1)

	pid = PID(0.001, 100, 0.1, setpoint = 0)

	pid.output_limits = (0, 60)

	start_time = 0

flag1 = 0
flag2 = 0

f1 = open('HW6_Right.txt', 'w')
f2 = open('HW6_Left.txt', 'w')

while(True):

	if int(gpio.input(12)) != int(buttonBR):
		buttonBR = int(gpio.input(12))
		counterBR += 1

	if int(gpio.input(7)) != int(buttonFL):
		buttonFL = int(gpio.input(7))
		counterFL += 1

	if time.time() - start_time >= 0.001:
		control = pid(counterBR - counterFL)

		#print(control)
		#print(target, counterBR - counterFL, counterBR, counterFL)
		pwm2.ChangeDutyCycle(control)
		f1.write(str(buttonBR)+'\n')
		f2.write(str(buttonFL)+'\n')


	if counterBR == target:
		pwm1.stop()
		flag1 = 1
	if counterFL == target:
		pwm2.stop()
		flag2 = 1

	if flag1 == 1 and flag2 == 1:
		gameover()
		start_time = time.time()
		break

f1.close()
f2.close()

