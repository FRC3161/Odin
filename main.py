import pyzbar.pyzbar as pyzbar
import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', grayscale)

    decodedBarcode = pyzbar.decode(grayscale)
    if decodedBarcode:
        print(decodedBarcode.data)
        break
