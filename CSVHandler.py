import csv


class CSVHandler:
    def __init__(self, csvfile):
        self.writer = csv.writer(csvfile, dialect='excel')

    def write_to_csv(self, data):
        self.writer.writerow(data)
