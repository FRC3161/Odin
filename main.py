from QR import QR
from CSVHandler import CSVHandler

csvfile = open('data.csv', 'a')

qr_reader = QR()
csv_writer = CSVHandler(csvfile)

while True:
    data = qr_reader.decode(qr_reader.read_camera())
    if(data):
        csv_writer.write_to_csv(data)
        break

qr_reader.destroy_windows()
qr_reader.release_camera()
csvfile.close()