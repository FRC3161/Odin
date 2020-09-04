import os
import yaml

class DataHandler:

    def __init__(self, dataDirectory="data"):
        if not os.path.exists(dataDirectory):
            os.mkdir(dataDirectory)