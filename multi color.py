# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 18:43:43 2021

@author: Rewat
"""

import numpy as np
import cv2
  
  
# Capturing video through webcam
webcam = cv2.VideoCapture(0)
  
# Start a while loop
while(1):
      
    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()
  
    frame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
  
    # Set range for red color and 
    # define mask
    red_lower = np.array([136, 100, 100], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(frame, red_lower, red_upper)
  
    # Set range for green color and 
    # define mask
    green_lower = np.array([25, 100, 100], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(frame, green_lower, green_upper)
  
    # Set range for blue color and
    # define mask
    blue_lower = np.array([94, 100, 100], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(frame, blue_lower, blue_upper)
      
    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    kernal = np.ones((5, 5), "uint8")
      
    # For red color
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, 
                              mask = red_mask)
      
    # For green color
    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(imageFrame, imageFrame,
                                mask = green_mask)
      
    # For blue color
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = blue_mask)
   
    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
   
    if len(contours) > 0:
        c=max(contours , key=cv2.contourArea)
        (x,y) , radius = cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center = (int(M["m10"] / M["m00"]) , int(M["m01"] / M["m00"]))
        
        if radius > 10:
            cv2.circle(imageFrame , (int(x),int(y)) , int(radius) , (0,255,255 , 2))
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            print(center)
        
            
        
        
        
        
#FOR RED COLOR     
    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if(area > 300):
    #         M=cv2.moments(contour[0])
    #         print(M)
    #         # cx = int(M['m10']/M['m00'])
    #         # cy = int(M['m01']/M['m00'])
    #         # print(f' red x cord = {cx} , red y cord = {cy}')
            
    #         x, y, w, h = cv2.boundingRect(contour)
    #         imageFrame = cv2.rectangle(imageFrame, (x, y), 
    #                                    (x + w, y + h), 
    #                                    (0, 0, 255), 2)
              
            #print(f'red x cord= {x} , red y cord= {y}')
            
      
            
#FOR BLUE COLOR           
    contours, hierarchy = cv2.findContours(blue_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0:
        c=max(contours , key=cv2.contourArea)
        (x,y),radius = cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center = (int(M["m10"] / M["m00"]) , int(M["m01"] / M["m00"]))
        
        if radius > 10:
            cv2.circle(imageFrame , (int(x),int(y)) , int(radius) , (0,255,255 , 2))
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            print(center)
            
            
        
    
    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if(area > 300):
    #         x, y, w, h = cv2.boundingRect(contour)
    #         imageFrame = cv2.rectangle(imageFrame, (x, y), 
    #                                    (x + w, y + h), 
    #                                    (0, 0, 255), 2)
            
    #         print(f'blue x cord= {x} , blue y cord = {y}')
    
            
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break
        

        

            



    
    
   