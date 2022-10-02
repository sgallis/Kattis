#https://open.kattis.com/problems/walls

from math import hypot
from collections import deque
from itertools import combinations

def distance(x, y, xbis, ybis):
    return hypot(x-xbis, y-ybis)

def solution():
    l, w, n, r = map(int, input().split())
    cranes = []
    true_cranes = [] # cranes that reach at least one wall
    for _ in range(n):
        cranes.append(tuple(map(int, input().split())))
    # test if possible
    walls =  ((-l/2,0), (l/2, 0), (0,-w/2), (0, w/2))
    reach = set()
    for crane in cranes:
        reaches = []
        for i, wall in enumerate(walls):
            if distance(crane[0], crane[1], wall[0], wall[1]) <= r:
                reach.add(i)
                reaches.append(i)
        if reaches:
            true_cranes.append(tuple(reaches))
    if 0 not in reach or 1 not in reach or 2 not in reach or 3 not in reach:
        print("Impossible")
    # reach contient 0,1,2,3
    true_cranes = tuple(true_cranes)
    cranesbis = [i for i in range(len(true_cranes))]
    for i in range(1, len(true_cranes)+1):
        for cranes1 in combinations(cranesbis, i):
            reaches = set()
            for k in cranes1:
                for j in true_cranes[k]:
                    reaches.add(j)
            if 0 in reaches and 1 in reaches and 2 in reaches and 3 in reaches:
                print(i)
                return

solution()
        




