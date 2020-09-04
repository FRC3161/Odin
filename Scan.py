from QR import QR

class Scan:
    def __init__(self):
        self.qr_reader = QR()

    def scan(self):
        self.qr_reader.create_camera()
        scanned = False
        while not scanned:
            data = self.qr_reader.decode(self.qr_reader.read_camera())
            if data:
                # TODO Write to YAML
                pass

        self.qr_reader.destroy_windows()
        self.qr_reader.release_camera()
        return

    def cleanup(self):
        self.qr_reader.destroy_windows()
        self.qr_reader.release_camera()