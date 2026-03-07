import time
import psutil

BYTES_IN_MB = 1024 * 1024

class Collector:
    def __init__(self):
        self._last_net = psutil.net_io_counters()
        self._last_time = time.time()

    def collect(self):
        current_time = time.time()
        current_net = psutil.net_io_counters()
        elapsed = current_time - self._last_time

        if elapsed > 0:
            network_in_mb_s = round(
                (current_net.bytes_recv - self._last_net.bytes_recv) / elapsed / BYTES_IN_MB, 2
            )
            network_out_mb_s = round(
                (current_net.bytes_sent - self._last_net.bytes_sent) / elapsed / BYTES_IN_MB, 2
            )
        else:
            network_in_mb_s = 0.0
            network_out_mb_s = 0.0

        metrics = {
            "cpu": psutil.cpu_percent(interval=None),
            "ram": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage("C:\\").percent,
            "network_in_mb_s": network_in_mb_s,
            "network_out_mb_s": network_out_mb_s,
        }

        self._last_net = current_net
        self._last_time = current_time

        return metrics