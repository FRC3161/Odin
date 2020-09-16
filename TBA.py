import tbapy
import os

class TBA:
    def __init__(self, event):

        self.API_KEY = os.getenv('TBA_API_KEY')
        self.tba = tbapy.TBA(self.API_KEY)

        self.event = event

    def getstatus(self):
        # Using this to test if I set it up correctly
        print(self.API_KEY)
        print(self.tba.status())

    def verify_team(self, match_number, match_type, alliance, team):
        # Checks if a team is on the specified alliance in a given match
        match_data = self.tba.match(key=f"{self.event}_{match_type}m{match_number}")
        for t in match_data.alliances[alliance]['team_keys']:
            if f"frc{str(team)}" == t:
                return True
        return False

    def verify_score(self, match_number, match_type, alliance):
        # Verifies the score of a given alliance in a match
        match_data = self.tba.match(key=f"{self.event}_{match_type}m{match_number}")
        return match_data.alliances[alliance]['score']


    def get_match_score(self, match_number, match_type, alliance):
        match_data = self.tba.match(key=f"{self.event}_{match_type}m{match_number}")
        return match_data.alliances[alliance]['score']
