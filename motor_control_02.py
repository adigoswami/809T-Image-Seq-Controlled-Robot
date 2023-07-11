# Code for teleoperation four wheels of the robot and gripper (4-8) 
# Also using SODAR sensor

from motor_control_01 import*
from drive01 import*

def measureDistance():
	avg = 0
	for i in range(10):
		measure = distance()
		avg += measure
	return avg/10

def key_input(event):
	tf = 0.5
	if key_press.lower() == 'w':
		forward(tf)
		print("Distance:", measureDistance(), 'cm')
	elif key_press.lower() == 's':
		reverse(tf)
		print("Distance:", measureDistance(), 'cm')
	elif key_press.lower() == 'a':
		pivotleft(tf)
		print("Distance:", measureDistance(), 'cm')
	elif key_press.lower() == 'd':
		pivotright(tf)
		print("Distance:", measureDistance(), 'cm')
	else:
		print("Invalid Key Pressed !!!!")

init()
pwm = gpio.PWM(36, 50)
pwm.start(4)
time.sleep(2)
action = ['w','a','s','d']

for i in action:
	key_input(i)
	time.sleep(2)
	
'''while(True):
	print('w:Forward ||', 'a:Left ||', 's:Backwards ||', 'd:Right ||', 'g:Gripper ||', 'q:exit')
	key_press = input("Select Driving Mode for the Robot : ")
	if key_press == 'g':
		dutyCycle = float(input('Input Duty Cycle between 3.0 to 6.5: '))
		if dutyCycle <= 8 and dutyCycle >= 4:
			pwm.ChangeDutyCycle(dutyCycle)
			time.sleep(2)
		else:
			print('Duty Cycle Out of range!!!!!!!')
	elif key_press == 'q':
		pwm.stop()
		gpio.cleanup()
		break
	else:
		key_input(key_press)'''

