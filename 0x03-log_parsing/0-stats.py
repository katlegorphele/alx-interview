#!/usr/bin/python3

'''script that reads stdin line by line and computes metrics'''

from sys import stdin

total_file_size: int = 0
status_code_dict: dict = {}

try:
    # loop through keyboard input lines
    for line_no, line in enumerate(stdin):
        line_token: list = line.split()

        if len(line_token) != 9:
            continue

        ip_, _, _, _, _, _, request, status_code,  file_size = line_token

        try:
            status_code = int(status_code)
        except ValueError:
            continue

        total_file_size += int(file_size)

        if status_code in status_code_dict:
            status_code_dict[status_code] += 1
        else:
            status_code_dict[status_code] = 1

        if line_no % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_dict.keys()):
                print(f"{code}: {status_code_dict[code]}")
except KeyboardInterrupt as err:
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_dict.keys()):
        print(f'{code}: {status_code_dict[code]}')
    print(err)
