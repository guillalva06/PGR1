# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:07:21 2015

@author: User
"""

import cv2
import numpy as np

#Scaling is resizing the image, se puede 
#definir un factor para el resizing
#para encoger cv2.INTER_AREA
#para aumentar cv2.INTER_LINEAR

img = cv2.imread('messi5.jpg')
res = cv2.resize(img, None, fx=2,fy=2,interpolation = cv2.INTER_CUBIC)
cv2.imshow("Resize",res)
cv2.waitKey(0)
cv2.destroyAllWindows()