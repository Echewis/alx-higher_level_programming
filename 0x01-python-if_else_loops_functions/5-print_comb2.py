#!/usr/bin/python3
for numz in range(100):
    if numz != 99:
        print("{:02}".format(numz), end=", ")
    else:
        print("{}".format(numz))
