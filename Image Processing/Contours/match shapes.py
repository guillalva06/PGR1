# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:58:43 2015

@author: User
"""

import cv2
import numpy as np

im1 = cv2.imread('perro1.jpg')
im2 = cv2.imread('perro2.jpg')
im3 = cv2.imread('estrella1.jpg')
im4 = cv2.imread('elefante.jpg')

img1 = cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(im3,cv2.COLOR_BGR2GRAY)
img4 = cv2.cvtColor(im4,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
ret, thresh3 = cv2.threshold(img3, 127, 255,0)
ret, thresh4 = cv2.threshold(img4, 127, 255,0)
#erosion sobre las imagenes ya binarias
kernel = np.ones((5,5),np.uint8)
thresh = cv2.erode(thresh,kernel,iterations = 1)
thresh2 = cv2.erode(thresh2,kernel,iterations = 1)
thresh3 = cv2.erode(thresh3,kernel,iterations = 1)
thresh4 = cv2.erode(thresh4,kernel,iterations = 1)
#Ver las imagenes binarias y erosionadas
cv2.imshow("Img1",thresh)
cv2.imshow("Img2",thresh2)
cv2.imshow("Img3",thresh3)
cv2.imshow("Img4",thresh4)
cv2.waitKey(0)
cv2.destroyAllWindows()

_, contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
_, contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]
_, contours,hierarchy = cv2.findContours(thresh3,2,1)
cnt3 = contours[0]
_, contours,hierarchy = cv2.findContours(thresh4,2,1)
cnt4 = contours[0]

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print ret
ret = cv2.matchShapes(cnt1,cnt3,1,0.0)
print ret
ret = cv2.matchShapes(cnt4,cnt3,1,0.0)
print ret