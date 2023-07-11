import numpy as np
import os 
import cv2
import imutils
import glob

# Snip/Region-of-Interest dimensions
lm = 90; aa = 385; bb = 400 ; cc = 45; rc  = 130

# Snip region of interest
def snip_image(img):
    cv2.rectangle(img, (lm, img.shape[0] - cc), (img.shape[1] - rc , img.shape[0] - aa), (255, 255, 255))
    snip = img[(img.shape[0] - aa):(img.shape[0] - cc), (lm):(img.shape[1] - rc)]
    return snip


#sorts tbe frames of the video in the folder according to the file number
def sortKeyFunc(s):
    return int(os.path.basename(s)[:-4])

img_array = []
path = "/Users/sukoon/enpm809T/fake_data/heatmaps/"

# path.sort(key=sortKeyFunc)

for i in range(1, 8):
	img = cv2.imread(path + str(i) + '.jpg')
	img = snip_image(img)
	#img = imutils.resize(img, width = 480)
	#blank = np.zeros((480,640))
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	# cv2.imshow("converted to HSV",hsv)

	lower_red = np.array([0, 130, 20]) 
	upper_red = np.array([255, 255, 255])
	mask = cv2.inRange(hsv, lower_red , upper_red);
	res = cv2.bitwise_and(hsv,hsv, mask= mask)
	ret,thresh2= cv2.threshold(hsv,127,255,cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	hull_list = []
	for i in range(len(contours)):
		hull = cv2.convexHull(contours[i])
		hull_list.append(hull)
	for i in range(len(contours)):
		cv2.drawContours(img, hull_list,i, (0,0,255),2)
		# cv2.imshow("Masking",mask)
		# cv2.imshow("Blobs",img)
		blobs = len(contours)
	print("No. of blobs detected: ", blobs)
	img_array.append(blobs)

print(img_array)

