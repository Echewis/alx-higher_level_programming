#!/usr/bin/python3
a = 0
for ch in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(ch - a)), end="")
    a = 32 if a == 0 else 0
