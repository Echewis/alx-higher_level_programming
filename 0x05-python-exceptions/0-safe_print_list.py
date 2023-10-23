#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    try:
        for a in range(x):
            print(my_list[a], end="")
            total += 1
    except IndexError:
        pass
    finally:
        print()
        return (total)
