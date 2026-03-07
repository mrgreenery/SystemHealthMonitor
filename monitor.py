import time

import collector
import display
import evaluator


class Monitor:
    def run(self):
        metric_collector = collector.Collector()
        metric_evaluator = evaluator.Evaluator()
        metric_display = display.Display()

        monitored_metrics = [
            ("CPU", "cpu", "%"),
            ("RAM", "ram", "%"),
            ("Disk", "disk", "%"),
        ]

        with metric_display.live:
            try:
                while True:
                    metrics = metric_collector.collect()
                    metric_display.reset()

                    for label, key, unit in monitored_metrics:
                        status = metric_evaluator.check_metric(key, metrics[key])
                        metric_display.render(label, metrics[key], unit, status)

                    metric_display.render("Network In", metrics["network_in_mb_s"], " MB/s")
                    metric_display.render("Network Out", metrics["network_out_mb_s"], " MB/s")

                    metric_display.show()
                    time.sleep(1)

            except KeyboardInterrupt:
                pass