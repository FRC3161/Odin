from QR import QR
from pyzbar.pyzbar import ZBarSymbol
from DataHandler import DataHandler
from PIL import Image
from Verify import Verify

import sys

class Scan:
    def __init__(self, parser):
        self.qr_reader = QR()
        self.data_handler = DataHandler()
        self.parser = parser
        self.args = self.parser.parse_args()
        self.verify = None

    def scan(self):
        self.qr_reader.create_camera()
        scanned = False
        while not scanned:
            if self.args.image:
                data = self.qr_reader.decode(Image.open(f'{self.args.image}'), symbol_type=[ZBarSymbol.QRCODE])
            else:
                data = self.qr_reader.decode(self.qr_reader.read_camera(), symbol_type=[ZBarSymbol.QRCODE])

            if data:
                # TODO Refactor, design is iffy
                yaml_data = self.data_handler.readData(data)
                # TODO add match score to the scouting app lol
                self.verify = Verify(yaml_data['_score'], yaml_data['Match Number'])
                if self.verify.verify_offline():
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
