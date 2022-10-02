#https://open.kattis.com/problems/collapse

import sys
from copy import deepcopy

def loop(islands, islands_new):
    for i, x in enumerate(islands):
        if x == [0, 0]:
            pass
        else:
            T = 0
            for j in range(2, len(x), 2):
                if islands[x[j]] == [0, 0]:
                    pass
                else:
                    T += x[j + 1]
            if T < x[0]:
                islands_new[i] = [0, 0]
    return islands, islands_new

def solution():
    N = int(input())
    islands = [[0,0]]
    for line in sys.stdin:
        L = list(map(int, line.split()))
        T = L[0]
        K = L[1]
        islands.append(L)
    islands_new = deepcopy(islands)
    islands, islands_new = loop(islands, islands_new)
    while islands_new != islands:
        islands = deepcopy(islands_new)
        islands, islands_new = loop(islands, islands_new)
    print(N-islands_new.count([0, 0]) + 1)

solution()

