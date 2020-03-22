import pyzbar.pyzbar as pyzbar
import cv2

camera = cv2.VideoCapture(-1)

while True:
    ret, frame = camera.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', grayscale)

    decodedBarcode = pyzbar.decode(frame)
    if decodedBarcode:
        print(decodedBarcode[0].data)
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()