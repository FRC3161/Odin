from QR import QR
from CSVHandler import CSVHandler
import shutil
import time

class Scan:
    def __init__(self, dataFileName):
        self.csvfile = open(dataFileName, 'a')
        self.qr_reader = QR()
        self.csv_writer = CSVHandler(self.csvfile)
        # Backing up file every 10 scans
        self.scans = 0

    def scan(self):
        scanned = False
        while not scanned:
            data = self.qr_reader.decode(self.qr_reader.read_camera())
            if data:
                self.csv_writer.write_to_csv(data)
                scanned = True
        self.qr_reader.destroy_windows()
        self.qr_reader.release_camera()
        self.scans += 1
        if self.scans == 10:
            shutil.copy(self.csvfile, f"{self.csvfile}_{int(time.time())}.csv")
            self.scans = 0
        return

    def cleanup(self):
        self.qr_reader.destroy_windows()
        self.qr_reader.release_camera()
        self.csvfile.close()