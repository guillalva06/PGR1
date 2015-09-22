# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:34:04 2015

@author: User
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudokusmall.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[351,328],[1151,327],[1207,1062],[303,1064]])
pts2 = np.float32([[0,0],[800,0],[0,800],[800,800]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(800,800))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()