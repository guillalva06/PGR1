# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:01:42 2015

@author: User
"""

import cv2
import numpy as np
#Observar las banderas para conversion de
#colores en imagenes
#flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print flags

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    
    #Convert BGR to HSV    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color = np.uint8([[[0,255,0]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)            
    #define range of yellow cloro in HSV
    lower_yellow = np.array([hsv_color[0][0][0]-10,50,50])
    upper_yellow = np.array([hsv_color[0][0][0]+10,255,255])
    #lower_yellow = np.array([20,50,50])
    #upper_yellow = np.array([30,255,255])    
    #Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    #Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()