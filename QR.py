import pyzbar.pyzbar as pyzbar
import cv2

# TODO probably should refactor at some point

class QR:
    def __init__(self):
        self.ret = None
        self.frame = None
        self.decodedData = None
        self.grayscale = None
        self.camera = cv2.VideoCapture(0)

    def read_camera(self):
        self.ret, self.frame = self.camera.read()
        self.grayscale = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', self.grayscale)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            return

        return self.grayscale

    def decode(self, data, symbol_type):
        self.decodedData = pyzbar.decode(data, symbols=symbol_type)
        if self.decodedData:
            return self.decodedData[0].data.decode('utf-8').split(", ")
        else:
            return None

    def create_camera(self):
        self.camera = cv2.VideoCapture(0)

    def destroy_windows(self):
        cv2.destroyAllWindows()

    def release_camera(self):
        self.camera.release()
