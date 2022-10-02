#https://open.kattis.com/problems/doctorkattis

import sys
import heapq
import bisect

# [infection_level, arrive_order, name]
# put infection_level as a negative int

def solution():
    n = int(input())
    tas = []
    cats = dict()
    i = 0
    for line in sys.stdin:
        a = line.rstrip("\n")
        a = a.split()
        #print(tas)
        #print(f"command {a}")
        if int(a[0]) == 0: #arrive
            i += 1
            heapq.heappush(tas, [-int(a[2]), i, a[1]])
            cats.setdefault(a[1], [-int(a[2]), i])
        elif int(a[0]) == 1: #update
            increment = int(a[2])
            catName = a[1]
            #find the cat
            ind = bisect.bisect_left(tas, [cats[catName][0], cats[catName][1], catName])
            #print(ind)
            #update the tas and the dict
            cats[catName] = [cats[catName][0] - increment, cats[catName][1], catName]
            tas[ind] = [cats[catName][0], cats[catName][1], catName]
            heapq.heappush(tas, [cats[catName][0], cats[catName][1], catName])
        elif int(a[0]) == 2: #treated
            catName = a[1]
            #find the cat
            ind = bisect.bisect_left(tas, [cats[catName][0], cats[catName][1], catName]) + 1
            #print(ind)
            #update the tas
            tas[ind][1] = 0
        else: #query
            if not tas:
                sys.stdout.write(f"The clinic is empty\n")
            else:
                while tas[0][1] == 0:
                    heapq.heappop(tas)
                sys.stdout.write(f"{tas[0][2]}\n")

solution()