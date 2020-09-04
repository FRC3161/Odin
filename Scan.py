from QR import QR
from pyzbar.pyzbar import ZBarSymbol
from DataHandler import DataHandler

class Scan:
    def __init__(self):
        self.qr_reader = QR()
        self.data_handler = DataHandler()

    def scan(self):
        self.qr_reader.create_camera()
        scanned = False
        while not scanned:
            data = self.qr_reader.decode(self.qr_reader.read_camera(), symbol_type=[ZBarSymbol.QRCODE])
            if data:
                # TODO Refactor, design is iffy
                yaml_data = self.data_handler.readData(data)
                self.data_handler.writeData(yaml_data)
                # I remember there being some reason why I didn't use a break here
                # Either it didn't work or readability
                scanned = True

        self.qr_reader.destroy_windows()
        self.qr_reader.release_camera()
        return

    def cleanup(self):
        self.qr_reader.destroy_windows()
        self.qr_reader.release_camera()
