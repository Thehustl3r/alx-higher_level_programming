#!/usr/bin/python3
""" Mugisha Prosper"""
import sys

total_file_size = 0
status_code_array = {}

try:
    count = 0
    for line in sys.stdin:
        av = line.split()

        file_size = int(av[-1])

        total_file_size += file_size

        status_code = av[-2]
        if status_code in status_code_array:
            status_code_array[status_code] += 1
        else:
            status_code_array[status_code] = 1
        if count % 10 == 0:
            print(f"File size: {total_file_size}")
            sorted_status_codes = sorted(status_code_array.keys())
            for code in sorted_status_codes:
                i = status_code_array[code]
                print(f"{code}: {i}")

except KeyboardInterrupt:
    pass
print(f"File size: {total_file_size}")
sorted_status_codes = sorted(status_code_array.keys())

for code in sorted_status_codes:
    i = status_code_array[code]
    print(f"{code}: {i}")
