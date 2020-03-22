import pyzbar.pyzbar as pyzbar
import cv2
import csv
import pathlib

camera = cv2.VideoCapture(-1)

"""
if not pathlib.Path('data.csv').is_file():
    f = open('data.csv', 'a')
    f.write("Name,Match Number,Team Number,Alliance,Preloaded Cells,High Port Auto,Low Port Auto,Missed Auto,High Port Teleop,Low Port Teleop,Missed Teleop,Robot Attitude,Colour Wheel Done,Colour Wheel Landed on Colour,Colour Wheel Was Rotated,Did Climb,Balanced,Number of Climbs,Notes,Confidence")
    f.close()
"""

while True:
    ret, frame = camera.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', grayscale)

    decodedBarcode = pyzbar.decode(frame)
    if decodedBarcode:
        scoutingData = decodedBarcode[0].data.decode('utf-8').split(", ")
        with open('data.csv', 'a') as out_file:
            wr = csv.writer(out_file)
            wr.writerow(scoutingData)
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()