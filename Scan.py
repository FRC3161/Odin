from QR import QR
from pyzbar.pyzbar import ZBarSymbol

class Scan:
    def __init__(self):
        self.qr_reader = QR()

    def scan(self):
        self.qr_reader.create_camera()
        scanned = False
        while not scanned:
            data = self.qr_reader.decode(self.qr_reader.read_camera(), symbol_type=[ZBarSymbol.QRCODE])
            if data:
                # TODO Write to YAML
                return data
                # I remember there being some reason why I didn't use a break here
                # Either it didn't work or readability
                scanned = True

        self.qr_reader.destroy_windows()
        self.qr_reader.release_camera()
        return

    def cleanup(self):
        self.qr_reader.destroy_windows()
        self.qr_reader.release_camera()