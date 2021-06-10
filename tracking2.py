# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:59:55 2021

@author: Rewat
"""

from collections import deque
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,help="max buffer size")
args = vars(ap.parse_args())

colorLower = (-10, 100, 100)
colorUpper = (10, 255, 255)
pts = deque(maxlen=args["buffer"])

def mapObjectPosition (x, y):
    print ("[INFO] Object Center coordenates at X0 = {0} and Y0 =  {1}".format(x, y))

if not args.get("video", False):
    camera = cv2.VideoCapture(0)
    
(grabbed, frame) = camera.read()
frame = imutils.resize(frame, width=1200)
	#frame = imutils.rotate(frame, angle=180)
    # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
mask = cv2.inRange(hsv, colorLower, colorUpper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
	
	# find contours in the mask and initialize the current
	# (x, y) center of the ball
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
		
center = None

if len(cnts) > 0:
    c = max(cnts, key=cv2.contourArea)
    ((x,y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    map()
    
    
    if radius > 10:
        cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)
        mapObjectPosition(int(x) , int(y))
        
pts.appendleft(center)

for i in range(1, len(pts)):
    if pts[i - 1] is None or pts[i] is None:
        continue
    
    thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
    cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
    
cv2.imshow('frame' , frame)
k = cv2.waitKey(5) & 0xFF

while(1):
    k=cv2.waitKey(0)
    if k==27:
        break
    
cv2.destroyWindow()
    

				
	
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    