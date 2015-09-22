# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:27:03 2015

@author: User
"""
import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
b,g,r = cv2.split(img)
cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red',r)
cv2.waitKey(0)
cv2.destroyAllWindows()
#volver 0 todos los pixeles del canal azul
b[::]=0
cv2.imshow("Blue",b)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = cv2.merge((b,g,r))
cv2.imshow("Resultado",img)
cv2.waitKey(0)
cv2.destroyAllWindows()