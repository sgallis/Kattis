#https://open.kattis.com/contests/xrjk7f/problems/growlinggears

import sys

def solution():
    n = int(input())
    for _ in range(n):
        gears = int(sys.stdin.readline().rstrip("\n"))
        maxl = []
        for _ in range(gears):
            a, b, c = map(int, sys.stdin.readline().split())
            R = b/2/a
            maxl.append(-a*R*R + b*R + c)
        i = 0
        for j in range(gears):
            if maxl[j] > maxl[i]:
                i = j
        sys.stdout.write(f"{i + 1}\n")

solution()