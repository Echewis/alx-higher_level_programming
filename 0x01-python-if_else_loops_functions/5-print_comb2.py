#!/usr/bin/python3
for numz in range(100):
    print("{:02}".format(numz), end="")
    if numz != 99:
        print(", ", end="")
print()
