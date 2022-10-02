#https://open.kattis.com/problems/hermits

import sys

N = int(input())
streets = list(map(int, input().split()))
streets_update = streets.copy()
M = int(input())
for line in sys.stdin:
    i, j = map(int, line.rstrip("\n").split())
    streets_update[i-1] += streets[j-1]
    streets_update[j-1] += streets[i-1]

ind = 1
population = streets_update[0]
for i in range(1, len(streets_update)):
    if streets_update[i] < population:
        population = streets_update[i]
        ind = i + 1
print(ind)

