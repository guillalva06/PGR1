import cv2
import numpy as np
img = cv2.imread('messi5.jpg')
px = img[100,100]
#px is a matrix of 3 dimensions RGB
print px
# accessing only blue pixel
blue = img[100,100,0]
print blue
# Modify pixel values
img[100,100] = [255,255,255]
print img[100,100]
#mejor acceso a los datos se hace con
#array.item(), el problema es que solo 
#retorna un escalar, para tomar los valores RGB
#debe llamarse 3 veces
print img.item(10,10,0)
print img.item(10,10,1)
print img.item(10,10,2)
print img[10,10]

#Propiedades de las imagenes
#img.shape retorna una tupla con el numero
# de filas, columnas y canales(si la imagen es
# a color)
print img.shape

#img.size retorna la cantidad de pixeles de la imagen
print img.size

#img.dtype retorna el tipo de imagen que es
print img.dtype

#Region of Images, observar solo ciertas regiones de la imagen,
#los ojos siempre estan en caras.
ball = img[280:340,330:390]
img[273:333,100:160] = ball
cv2.imshow('Imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Dividir o unir canales de imagenes


