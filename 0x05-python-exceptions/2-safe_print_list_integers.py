#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    for a in range(x):
        try:
            if isinstance(my_list[a], int):
                print("{:d}".format(my_list[a]), end="")
                total += 1
        except (TypeError, ValueError):
            continue
    print()
    return (total)
