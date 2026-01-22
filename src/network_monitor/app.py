import os

import psutil
import time
from cyclopts import App

cli_app = App()

MB = 1_000_000


@cli_app.default()
@cli_app.command()
def monitor_network_rate(interval=1):
    """
    Monitors the network transfer rate (bytes/sec) for each interface over a given interval.
    """
    print(f"Monitoring network activity every {interval} second(s)... Press Ctrl+C to stop.")

    dl_at_start = {}
    ul_at_start = {}

    try:
        while True:
            # Get initial stats
            old_stats = psutil.net_io_counters(pernic=True)
            time.sleep(interval)
            # Get new stats after the interval
            new_stats = psutil.net_io_counters(pernic=True)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("-" * 110)
            print(f"{'Interface':<20} | {'DL Rate (Mbit/s)':<20} | {'UL Rate (Mbit/s)':<20} | {'MB downloaded':<20} | {'MB uploaded':<20}")
            print("-" * 110)

            for idx, interface in enumerate(new_stats):
                if interface in old_stats:
                    if not old_stats[interface].bytes_recv and not new_stats[interface].bytes_recv:
                        continue
                    download_rate = (new_stats[interface].bytes_recv - old_stats[interface].bytes_recv) / interval * 8 / MB
                    upload_rate = (new_stats[interface].bytes_sent - old_stats[interface].bytes_sent) / interval * 8 / MB

                    if not dl_at_start.get(interface):
                        dl_at_start[interface] = new_stats[interface].bytes_recv
                    if not ul_at_start.get(interface):
                        ul_at_start[interface] = new_stats[interface].bytes_sent

                    downloaded_megabytes = (new_stats[interface].bytes_recv - dl_at_start[interface]) / MB
                    uploaded_megabytes = (new_stats[interface].bytes_sent - ul_at_start[interface]) / MB

                    print(f"{interface:<20} | {download_rate:<20.2f} | {upload_rate:<20.2f} | {downloaded_megabytes:<20.2f} | {uploaded_megabytes:<20.2f}")

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


def main():
    cli_app()


if __name__ == "__main__":
    main()