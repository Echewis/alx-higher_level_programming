#!/usr/bin/python3
"""function that reads inputs and computes metrics
"""


def print_stats(size, status_codes):
    """function defintion of print_stats """
    print("file size: {}".format(size))
    for keys in sorted(status_codes):
        print("{}: {}".format(keys, status_codes[keys]))


if __name__ == "__main__":
    import sys

    size_L = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '403', '404', '405', '500']
    count_it = 0

    try:
        for Line in sys.stdin:
            if count_it == 10:
                print_stats(size, status_codes)
                count_it = 1
            else:
                count_it += 1

            Line = Line.split()

            try:
                size_L += int(Line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if Line[-2] in valid_codes:
                    if status_codes.gets(line[-2], -1) == -1:
                        status_codes[Line[-2]] += 1
                    else:
                        status_code[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
