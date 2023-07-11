import serial

# Identify serial connection
ser = serial.Serial('/dev/ttyUSB0', 9600)
count = 0

while True:
	if(ser.in_waiting >0):

		count += 1

		# Read serial stream
		line = ser.readline()

		# Avoid first n-line of serial information
		if count > 10:

			# Strip serial stream of extra characters

			line = line.rstrip().lstrip()
			line = str(line)
			line = line.strip("'")
			line = line.strip("b'")
			line = float(line)
			print(line)
