#https://open.kattis.com/problems/bobby
import random
import sys
import math
def fcomb0(n, k):
    if k < 0 or k > n:
        return 0

    if k == 0 or k == n:
        return 1

    total_ways = 1
    for i in range(min(k, n - k)):
        total_ways = total_ways * (n - i) // (i + 1)

    return total_ways
def solution():
    n = int(input())
    for _ in range(n):
        R, S, X, Y, W = map(int, sys.stdin.readline().split())
        probawin = 0
        for i in range(X, Y + 1):
            probawin += pow((1 - (R - 1) / S), i) * pow(((R - 1)/ S), Y - i) * fcomb0(Y, i)
        probalose = 1 - probawin
        esperance = (W - 1) * probawin - probalose
        if esperance > 0:
            sys.stdout.write("yes\n")
        else:
            sys.stdout.write("no\n")

solution()
