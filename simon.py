#https://open.kattis.com/problems/simon

import sys

T = int(input())
for line in sys.stdin:
    a = line.rstrip("\n").split()
    if len(a) < 2:
        sys.stdout.write("\n")
    elif a[0] != "simon" or a[1] != "says":
        sys.stdout.write("\n")
    else:
        sys.stdout.write(" ".join(a[2:])+"\n")
