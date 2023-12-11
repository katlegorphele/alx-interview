#!/usr/bin/python3

"""script that reads stdin line by line and computes metrics"""

from sys import stdin

total_file_size: int = 0
status_code_dict: dict = {}

#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats(signal=None, frame=None):
    """Print statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


# Set signal handler for CTRL+C
signal.signal(signal.SIGINT, print_stats)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            size = int(parts[-1])
            code = int(parts[-2])
            total_size += size
            if code in status_codes:
                status_codes[code] += 1
        except:
            continue

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass
finally:
    print_stats()
