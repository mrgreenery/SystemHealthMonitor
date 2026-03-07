from rich.console import Console
from rich.live import Live
from rich.table import Table

class Display:
    def __init__(self):
        self.console = Console()
        self.table = self._create_table()
        self.live = Live(self.table, refresh_per_second=2)

    def _create_table(self):
        table = Table(title="System Health Monitor")
        table.add_column("Metric", style="cyan", no_wrap=True, justify="right")
        table.add_column("Value", style="cyan", no_wrap=True, justify="right")
        table.add_column("Status", style="cyan", no_wrap=True, justify="right")
        return table

    def render(self, name, value, unit="", status="-"):
        if status == "ALERT":
            status_text = "[bold red]ALERT[/bold red]"
        elif status == "OK":
            status_text = "[bold green]OK[/bold green]"
        else:
            status_text = status

        self.table.add_row(name, f"{value}{unit}", status_text)

    def show(self):
        self.live.update(self.table, refresh=True)

    def reset(self):
        self.table = self._create_table()





