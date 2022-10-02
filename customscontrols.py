# https://open.kattis.com/problems/customscontrols

import heapq
import math
import sys

n,m,k = map(int, input().split())

time = list(map(int, input().split()))
paths = [None] + [[]for _ in range(n)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    paths[i].append(j)
    paths[j].append(i)

visited = set()
start = 1
f = [(0, start)]
while f:
    (D, v) = heapq.heappop(f)
    visited.add(v)