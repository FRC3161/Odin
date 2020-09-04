import os
import yaml

class DataHandler:

    def __init__(self, dataDirectory="data"):
        self.dataDirectory = dataDirectory

        if not os.path.exists(self.dataDirectory):
            os.mkdir(self.dataDirectory)

    def readData(self, data: str):
        # TODO I'm assuming the data is in a certain order, is there a better way or do I just need to make this assumption?
        # TODO Bruh moment, refactor this please
        # TODO Check data most likely in (an)other function(s)
        # TODO Possibly look into re-ordering data into a more logical fashion, right now important field (ie. team number)
        # TODO HARDCODING LMAOOOOO HAHAHAHAH
        # are in random locations
        data_list = data.split(",")
        data_dict = {
            "Team Name": data_list[0],
            "Match Number": int(data_list[1]),
            "Match Type": data_list[2],
            "Team Number": int(data_list[3]),
            "Alliance": data_list[4],
            "Preload": int(data_list[5]),
            "High Port Auto": int(data_list[6]),
            "Low Port Auto": int(data_list[7]),
            "Missed Auto": int(data_list[8]),
            "High Port Teleop": int(data_list[9]),
            "Low Port Teleop": int(data_list[10]),
            "Missed Teleop": int(data_list[11]),
            "Robot Attitude": data_list[12],
            "Colour Wheel Done": data_list[13],
            "Colour Wheel Landed": data_list[14],
            "Colour Wheel Was Rotated": data_list[15],
            "Climb": data_list[16], # TODO possibly a boolean, look into this
            "Balanced": data_list[17],
            "Number of Climbs": int(data_list[18]),
            "Notes": data_list[19]
        }

        return yaml.dump(data_dict)

    def writeData(self, data):
        # Writes the YAML to a file
        pass