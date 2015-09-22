# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:17:08 2015

@author: User
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('taj-mahal.jpg')

#Existen 4 tipos de filtros en opencv
#promedio
blur = cv2.blur(img,(5,5))
#Gausiano
blur2 = cv2.GaussianBlur(img,(5,5),0)
#Mediana
blur3 = cv2.medianBlur(img,5)
#Bilateral
blur4 = cv2.bilateralFilter(img,9,75,75)
plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.subplot(232),plt.imshow(blur),plt.title('Average')
plt.subplot(233),plt.imshow(blur2),plt.title('Gaussian')
plt.subplot(234),plt.imshow(blur3),plt.title('Median')
plt.subplot(235),plt.imshow(blur4),plt.title('Bilateral')
plt.show()