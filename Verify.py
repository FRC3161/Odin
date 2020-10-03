import Constants

class Verify:
    def __init__(self):
        pass

    #TODO give better name
    def score_isnumeric(self, score):
        # Could use isnumeric() here, but it will throw an error if score is an integer
        try:
            int(score)
        except ValueError:
            return False
        return True

    def check_score_bounds(self, score):
        if (Constants.SCORE_MIN > score) or (Constants.SCORE_MAX < score):
            return False
        return True

    # pretty much just copypaste but it's for readability
    def match_isnumeric(self, matchno):
        try:
            int(match)
        except ValueError:
            return False
        return True

    def check_match_bounds(self, matchno):
        if (Constants.MATCH_MIN > matchno) or (Constants.MATCH_MAX < matchno):
            return False
        return True

    def verify_offline(self, score, matchno):
        if self.score_isnumeric(score) and self.check_score_bounds(score) and self.match_isnumeric(matchno) and self.check_match_bounds(matchno):
            return True
        return False