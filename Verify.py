class Verify:
    def __init__(self):
        pass

    def check_if_score_is_numeric(self, score):
        try:
            int(score)
        except ValueError:
            return False
        return True

    def verify_offline(self):
        pass