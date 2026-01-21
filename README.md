# 🛜 Network Monitor 

## Background

Just needed a very simplistic network monitor.

## Installation and usage

```shell
uv tool install https://github.com/engdan77/network_monitor.git
network-monitor --help
Usage: network-monitor COMMAND [ARGS]

Monitors the network transfer rate (bytes/sec) for each interface over a given
interval.

╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ monitor-network-rate  Monitors the network transfer rate (bytes/sec) for     │
│                       each interface over a given interval.                  │
│ --help (-h)           Display this message and exit.                         │
│ --version             Display application version.                           │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Parameters ─────────────────────────────────────────────────────────────────╮
│ INTERVAL --interval  [default: 1]                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
```