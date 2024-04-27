#!/usr/bin/python3
import sys

def print_statistics(file_size, status_codes):
    """Prints statistics."""
    print("File size: {}".format(file_size))
    for status_code, count in sorted(status_codes.items()):
        print("{}: {}".format(status_code, count))

def main():
    """Main function."""
    count = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            count += 1
            tokens = line.split()
            file_size += int(tokens[-1])
            status_code = tokens[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1

            if count % 10 == 0:
                print_statistics(file_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)
        raise

if __name__ == "__main__":
    main()

