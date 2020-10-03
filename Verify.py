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

    def verify_offline(self):
        pass