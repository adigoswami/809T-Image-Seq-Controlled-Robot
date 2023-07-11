
import RPi.GPIO as gpio
import time
import os
import sys
import cv2
import imutils

# Define Pin Allocation
trig = 16
echo = 18

def distance():
	#gpio.setmode(gpio.BOARD)
	#gpio.setup(trig, gpio.OUT)
	#gpio.setup(echo, gpio.IN)

	# Ensure output has no value
	gpio.output(trig, False)
	time.sleep(0.01)

	# Generate trigger pulse
	gpio.output(trig, True)
	time.sleep(0.000010)
	gpio.output(trig, False)

	# Generate echo time signal
	while gpio.input(echo) == 0:
		pulse_start = time.time()

	while gpio.input(echo) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	# Convert time to distance
	distance = pulse_duration*17150
	distance = round(distance, 2)

	# Cleanup gpio pins & return distance estimate
	#gpio.cleanup()
	return distance

if __name__ == '__main__':

	avg = 0
	for i in range(10):
		measure = distance()
		print("Distance: ", measure, "cm")
		avg = avg + measure
	avg = avg/10
	print("Average is: ", avg)

	img_name = "20200220test.jpg"
	os.system('raspistill -w 640 -h 480 -o ' + img_name) 

	img = cv2.imread("20200220test.jpg")
	font = cv2.FONT_HERSHEY_COMPLEX_SMALL
	cv2.putText(img, str(avg), (50, 50), font, 1, (255, 0, 0), 2)
	cv2.imshow("Image", img)
	cv2.waitKey(0)

	print("Finished Working!!")
