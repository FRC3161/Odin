import os
import yaml
import datetime

class DataHandler:
    def __init__(self, data_directory="data"):
        self.data_directory = data_directory

        if not os.path.exists(self.data_directory):
            os.mkdir(self.data_directory)

    def readData(self, data: str):
        # TODO I'm assuming the data is in a certain order, is there a better way or do I just need to make this assumption?
        # TODO Bruh moment, refactor this please
        # TODO Check data most likely in (an)other function(s)
        # TODO Possibly look into re-ordering data into a more logical fashion, right now important field (ie. team number)
        # TODO HARDCODING LMAOOOOO HAHAHAHAH
        # are in random locations
        data_list = data.split(",")
        data_dict = {
            "Scouter Name": data_list[0],
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

    # TODO Figure out YAML type hinting
    def writeData(self, yaml_data):
        # TODO Refactor, this is going to be a real stinker
        # TODO Generate some test data to test this out
        data = yaml.load(yaml_data, Loader=yaml.FullLoader)
        # splitting this to make it cleaner
        # filename format: teamnumber_matchtype_matchnumber_scouter_date_time.yaml
        # date/time are when the data is entered, so don't use it to determine a match number
        filename = f"{data['Team Number']}_{data['Match Type']}_{data['Match Number']}_{data['Scouter Name']}_{datetime.datetime.date(datetime.datetime.now())}_{datetime.datetime.time(datetime.datetime.now())}.yaml"
        f = open(f"{self.data_directory}/{filename}", "w")
        f.write(yaml_data)
        f.close()



        