from config import THRESHOLDS


class Evaluator:
    def check_metric(self, name, value):
        threshold = THRESHOLDS.get(name)

        if threshold is None:
            return "-"

        if value >= threshold:
            return "ALERT"

        return "OK"