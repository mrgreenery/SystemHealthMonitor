from config import THRESHOLDS

class Evaluator:
        def check_metric(self, name, value):
            status = "ALERT" if value >= THRESHOLDS[name] else "OK"
            return status
