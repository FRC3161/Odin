import Constants

class Verify:
    def __init__(self):
        pass

    #TODO give better name
    def check_if_score_is_numeric(self, score):
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