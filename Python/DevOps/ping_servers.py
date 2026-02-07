import subprocess
import platform
import time
from datetime import datetime

IPS = [
    "10.10.0.205",
     "10.10.0.174",
     "10.10.0.12",
     "57.128.41.185",
     "146.59.243.9",
     "93.47.100.131",
     "152.228.208.67"
]

PING_INTERVAL = 10  # seconds

def ping(ip):
    system = platform.system().lower()

    if system == "windows":
        cmd = ["ping", "-n", "1", "-w", "1000", ip]
    else:
        cmd = ["ping", "-c", "1", "-W", "1", ip]

    result = subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0


def main():
    while True:
        for ip in IPS:
            if ping(ip):
                print(f"[{datetime.now()}] OK     {ip}")
            else:
                print(f"[{datetime.now()}] ERROR  {ip} is unreachable")
        print("-" * 40)
        time.sleep(PING_INTERVAL)


if __name__ == "__main__":
    main()