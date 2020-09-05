import os
import yaml
import time
from pathlib import Path

class DataHandler:
    def __init__(self, data_directory="data"):
        self.data_directory = data_directory

        if not os.path.exists(self.data_directory):
            os.mkdir(self.data_directory)

    def readData(self, data: list):
        # TODO I'm assuming the data is in a certain order, is there a better way or do I just need to make this assumption?
        # TODO Bruh moment, refactor this please
        # TODO Check data most likely in (an)other function(s)
        # TODO Possibly look into re-ordering data into a more logical fashion, right now important field (ie. team number)
        # TODO HARDCODING LMAOOOOO HAHAHAHAH
        # are in random locations
        data_dict = {
            "Scouter Name": data[0],
            "Match Number": int(data[1]),
            "Match Type": data[2],
            "Team Number": int(data[3]),
            "Alliance": data[4],
            "Preload": int(data[5]),
            "High Port Auto": int(data[6]),
            "Low Port Auto": int(data[7]),
            "Missed Auto": int(data[8]),
            "High Port Teleop": int(data[9]),
            "Low Port Teleop": int(data[10]),
            "Missed Teleop": int(data[11]),
            "Robot Attitude": data[12],
            "Colour Wheel Done": data[13],
            "Colour Wheel Landed": data[14],
            "Colour Wheel Was Rotated": data[15],
            "Climb": data[16], # TODO possibly a boolean, look into this
            "Balanced": data[17],
            "Number of Climbs": int(data[18]),
            "Notes": data[19]
        }

        return yaml.dump(data_dict)

    # TODO Figure out YAML type hinting
    def writeData(self, yaml_data):
        # TODO Refactor, this is going to be a real stinker
        # TODO Generate some test data to test this out
        data = yaml.load(yaml_data, Loader=yaml.FullLoader)
        # splitting this to make it cleaner
        # filename format: teamnumber_matchtype_matchnumber_scouter_date_time.yaml
        # date/time are when the data is entered, so don't use it to determine a match number
        filename = f"{data['Team Number']}_{data['Match Type']}_{data['Match Number']}_{data['Scouter Name']}_{time.strftime('%Y-%m-%d')}_{time.strftime('%H-%M-%S')}.yaml"
        f = open(Path(f"{os.path.dirname(__file__)}/{self.data_directory}/{filename}"), "w+")
        f.write(yaml_data)
        f.close()



        