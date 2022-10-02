#https://open.kattis.com/problems/safehouses

import sys

def distance(a, b):
    return abs(a[0]- b[0]) + abs(a[1] - b[1])

def solution():
    spies = []
    houses = []
    x = 0
    for line in sys.stdin:
        row = line.rstrip("\n") 
        for y in range(len(line)):
            if line[y] == "H":
                houses.append((x, y))
            elif line[y] == "S":
                spies.append((x, y))
        x += 1
    distances = set()
    distances1 = set()  
    while spies:
        spy = spies.pop()
        distances1 = set()
        for h in houses:
            distances1.add(distance(spy, h))
        distances.add(min(distances1))
    print(max(distances))

solution()

    

