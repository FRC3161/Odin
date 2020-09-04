import os
import yaml

class DataHandler:

    def __init__(self, dataDirectory="data"):
        if not os.path.exists(dataDirectory):
            os.mkdir(dataDirectory)

    def readData(self, data: str):
        # Will just turn the data into YAML and return it
        pass

    def writeData(self):
        # Writes the YAML to a file
        pass