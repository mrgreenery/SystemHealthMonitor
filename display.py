from rich.console import Console
from rich.live import Live
from rich.table import Table

class Display:
    def __init__(self):
        self.console = Console()
        self.table = Table(title="System Health Monitor")
        self.table.add_column("Metric", style="cyan", no_wrap=True, justify="right")
        self.table.add_column("Value", style="cyan", no_wrap=True, justify="right")
        self.table.add_column("Status", style="cyan", no_wrap=True, justify="right")
        self.live = Live(self.table, refresh_per_second=2)

    def render(self, name, value, unit="", status="-"):
        self.table.add_row(name, f"{value}{unit}", status)

    def show(self):
        self.live.update(self.table, refresh=True)

    def reset(self):
        self.table = Table(title="System Health Monitor")
        self.table.add_column("Metric", style="cyan", no_wrap=True, justify="right")
        self.table.add_column("Value", style="cyan", no_wrap=True, justify="right")
        self.table.add_column("Status", style="cyan", no_wrap=True, justify="right")
        self.live.update(self.table)





