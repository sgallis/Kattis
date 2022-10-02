#https://open.kattis.com/problems/jackpot

import sys
from math import gcd

def ppcm(a, b):
    return a * b // gcd(a, b)

def solution():
    n = int(input())
    for _ in range(n):
        wheels = int(input())
        periods = list(map(int, sys.stdin.readline().split()))
        a = periods[0]
        for b in periods[1:]:
            a = ppcm(a, b)
        if a > 10**9:
            sys.stdout.write("More than a billion.\n")
        else:
            sys.stdout.write(f"{a}\n")

solution()