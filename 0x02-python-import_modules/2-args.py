#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    len_arg = len(sys.argv)
    if len_arg == 1:
        print("{} arguments.".format(len_arg - 1))
    else:
        print("{} arguments:".format(len_arg - 1))
    for a in range(1, len_arg):
        print("{}: {}".format(a, sys.argv[a]))
