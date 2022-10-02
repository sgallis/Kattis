#https://open.kattis.com/problems/fractalarea

import math
import sys

for _ in range(int(input())):
    r, n = map(int, sys.stdin.readline().rstrip("\n").split())
    if n == 1:
        sys.stdout.write(f"{math.pi*r*r}\n")
    elif n == 2:
        sys.stdout.write(f"{math.pi*r*r*2}\n")
    else:
        sys.stdout.write(f"{math.pi*r*r*(2+3*(1-pow(3/4,n-2)))}\n")

