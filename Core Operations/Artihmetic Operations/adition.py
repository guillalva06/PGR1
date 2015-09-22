# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:36:06 2015

@author: User
"""

#Image addition
#cv2.add() es saturado mientras que numpy
#es modulo

import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([10])
print cv2.add(x,y)
print x+y
img1 = cv2.imread('ml.png')
img2 = cv2.imread('opencv-logo.png')
print img1.shape
print img2.shape
imgR = cv2.add(img1,img2)
cv2.imshow('Suma cv2',imgR)
cv2.imshow('Suma np', img1+img2)
cv2.waitKey(0)
cv2.destroyAllWindows()