#!/usr/bin/python3

import sys
def main():
    args = sys.argv[1:]
    result = 0
    for arg in args:
        result += int(arg)
        print("{}".format(result - 1))
    
if __name__ == '__main__':
   main()
