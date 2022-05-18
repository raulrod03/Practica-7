from matplotlib import pyplot as plt
from matplotlib import pylab 
import cv2
import imutils
import numpy as np

#img1 = cv2.VideoCapture(7)

img1 = cv2.imread('FR.jpg', 1)
img1hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
low_red = np.array([161, 155, 84])
high_red = np.array([179, 255, 255])
red_mask = cv2.inRange(img1hsv, low_red, high_red)
red = cv2.bitwise_and(img1hsv,img1hsv, mask=red_mask)
kernel2 = np.ones((5,5), np.uint8)
kernel = np.ones((15,15), np.float)/255

opening_red = cv2.morphologyEx(red, cv2.MORPH_OPEN, kernel2)
closing_red = cv2.morphologyEx(red, cv2.MORPH_CLOSE, kernel2)

low_blue = np.array([94, 80, 100])
high_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(img1hsv, low_blue, high_blue)
blue = cv2.bitwise_and(img1hsv, img1hsv, mask=blue_mask)
opening_blue = cv2.morphologyEx(blue, cv2.MORPH_OPEN, kernel2)
closing_blue = cv2.morphologyEx(blue, cv2.MORPH_CLOSE, kernel2)

low_green = np.array([40, 52, 72])
high_green = np.array([110, 255, 255])
green_mask = cv2.inRange(img1hsv, low_green, high_green)
green = cv2.bitwise_and(img1hsv, img1hsv, mask=green_mask)
opening_green = cv2.morphologyEx(green, cv2.MORPH_OPEN, kernel2)
closing_green = cv2.morphologyEx(green, cv2.MORPH_CLOSE, kernel2)

#while(1):
    #_, frame = img1.read()
img1hsv = cv2.resize(img1,(400,300))

red = cv2.resize(red,(400,300))
opening_red  = cv2.resize(opening_red ,(400,300))
closing_red = cv2.resize(closing_red,(400,300))
cv2.imshow('red',cv2.cvtColor(red,cv2.COLOR_HSV2BGR))
cv2.imshow('opening_red',cv2.cvtColor(opening_red,cv2.COLOR_HSV2BGR))
cv2.imshow('closing_red',cv2.cvtColor(closing_red,cv2.COLOR_HSV2BGR))
cv2.waitKey(0)

blue = cv2.resize(blue,(400,300))
opening_blue  = cv2.resize(opening_blue ,(400,300))
closing_blue = cv2.resize(closing_blue,(400,300))
cv2.imshow('blue',cv2.cvtColor(blue,cv2.COLOR_HSV2BGR))
cv2.imshow('opening_blue',cv2.cvtColor(opening_blue,cv2.COLOR_HSV2BGR))
cv2.imshow('closing_blue',cv2.cvtColor(closing_blue,cv2.COLOR_HSV2BGR))
cv2.waitKey(0)

green = cv2.resize(green,(400,300))
opening_green  = cv2.resize(opening_green ,(400,300))
closing_green = cv2.resize(closing_green,(400,300))
cv2.imshow('green',cv2.cvtColor(green,cv2.COLOR_HSV2BGR))
cv2.imshow('opening_green',cv2.cvtColor(opening_green,cv2.COLOR_HSV2BGR))
cv2.imshow('closing_green',cv2.cvtColor(closing_green,cv2.COLOR_HSV2BGR))
cv2.waitKey(0)

#img1.release()
