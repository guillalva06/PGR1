import numpy
import cv2

camara = cv2.VideoCapture(0)

while True:
    ret, frame = camara.read()
    cv2.imshow('camara', frame)
    if cv2.waitKey(1)== ord('q'):
        break

#Apaga el dispositivo en uso
camara.release()
cv2.destroyAllWindows()


    


