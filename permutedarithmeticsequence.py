# https://open.kattis.com/problems/permutedarithmeticsequence

import sys

n = int(input())

for _ in range(n):
    L = list(map(int, sys.stdin.readline().rstrip().split()))
    m, sequence = L[0], L[1:]
    diff = sequence[1]-sequence[0]
    arithmetic = True
    for i in range(2, len(sequence)):
        if sequence[i]-sequence[i-1] != diff:
            arithmetic = False
            break
    if arithmetic:
        sys.stdout.write("arithmetic\n")
    else:
        sequence.sort()
        diff = sequence[1]-sequence[0]
        arithmetic = True
        for i in range(2, len(sequence)):
            if sequence[i]-sequence[i-1] != diff:
                arithmetic = False
                break
        if arithmetic:
            sys.stdout.write("permuted arithmetic\n")
        else:
            sys.stdout.write("non-arithmetic\n")


