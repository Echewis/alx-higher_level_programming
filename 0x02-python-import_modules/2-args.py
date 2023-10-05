#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    len_arg = len(sys.argv)
    if len_arg == 1:
        print("{} arguments.".format(len_arg - 1))
    elif len_arg == 2:
        print("{} argument:".format(len_arg - 1))
    else:
        print("{} arguments:".format(len_arg - 1))
    for a in range(1, len_arg):
        print("{}: {}".format(a, sys.argv[a]))
        """When this code is executed, it will look like this:
        ./2-args.py Hello Welcome To The Best School
        6 arguments:
        1: Hello
        2: Welcome
        3: To
        4: The
        5: Best
        6: School
        """
