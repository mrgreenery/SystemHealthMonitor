# System Health Monitor

A lightweight, real-time system monitoring tool built in Python. Displays CPU, RAM, disk, and network usage in a live terminal dashboard

## Features

- Real-time polling of CPU, RAM, and disk usage using `psutil`
- Live network throughput (MB/s in and out)
- Threshold-based alerting with color-coded status
- Terminal dashboard using `rich`
- Separation of concerns across dedicated modules

## Project Structure

```
health-monitor/
├── main.py          # Entry point
├── monitor.py       # Controls the monitoring loop
├── collector.py     # Metrics collection (psutil)
├── evaluator.py     # Threshold evaluation
├── display.py       # Terminal UI (rich)
├── config.py        # Thresholds and settings
└── requirements.txt
```

## Requirements

- Python 3.8+
- pip

## Installation

```bash
git clone https://github.com/your-username/health-monitor.git
cd SystemHealthMonitor
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Press `Ctrl+C` to stop.

## Configuration

Edit `config.py` to adjust alert thresholds and refresh interval:

```python
THRESHOLDS = {
    "cpu": 80,   # percent
    "ram": 80,   # percent
    "disk": 90,  # percent
}

REFRESH_INTERVAL_SECONDS = 1
```

## Purpose

This project was built as a small exercise to practice:

- modular Python design
- separation of concerns
- working with system metrics
- building terminal interfaces with rich
