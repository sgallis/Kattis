#https://open.kattis.com/problems/trojke

import sys

def binom(n, k):
    if k < 0 or k > n:
        return 0

    if k == 0 or k == n:
        return 1

    total_ways = 1
    for i in range(min(k, n - k)):
        total_ways = total_ways * (n - i) // (i + 1)

    return total_ways

def lines(grid):
    s = 0
    for x in grid:
        occ = 0
        for letter in x:
            if letter != ".":
                occ += 1
        s += binom(occ, 3)
    return s

def columns

def solution():
    grid = []
    N = int(input())
    for line in sys.stdin:
        grid.append(line.rstrip("\n"))
    

solution()
