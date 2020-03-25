import tbapy
import os

class TBA:
    def __init__(self):
        self.API_KEY = os.getenv('TBA_API_KEY')
        self.tba = tbapy.TBA(self.API_KEY)

    def getstatus(self):
        # Using this to test if I set it up correctly
        print(self.API_KEY)
        print(self.tba.status())
