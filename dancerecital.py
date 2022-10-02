#https://open.kattis.com/problems/dancerecital

import sys
import heapq

def common(ini, final, routines):
    routine = routines[ini]
    routine2 = routines[final]
    a = [1 for i in routine if i in routine2]
    return sum(a)
    
def solution():
    R = int(input()) # R <= 10
    routines = [list(map(ord, line.rstrip("\n"))) for line in sys.stdin]
    # parcours de graphe avec dijkstra
    tas = []
    for i in range(R):
        heapq.heappush(tas, [0, 1, *[False if j != i else True for j in range(R)], i])
    seen = set()
    while tas:
        routine = heapq.heappop(tas)
        if tuple(routine) not in seen:
            seen.add(tuple(routine))
            if routine[1] == R:
                print(routine[0])
                return
            for i, x in enumerate(routine[2:-1]):
                if not x:
                    routine2 = routine.copy()
                    routine2[i+2] = True 
                    routine2[0] += common(routine[-1], i, routines)
                    routine2[-1] = i   
                    routine2[1] += 1
                    heapq.heappush(tas, routine2)
            

        




solution()
