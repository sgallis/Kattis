#https://open.kattis.com/problems/fodelsedagsmemorisering
import sys

def solution():
    n = int(input())
    d = dict()
    for _ in range(n):
        name, value, date = sys.stdin.readline().split()
        if date in d:
            if int(value) > d[date][1]:
                d[date] = [name, int(value)]
        else:
            d.setdefault(date, [name, int(value)])
        
    print(len(d))
    L = d.values()
    M = []
    for i in L:
        M.append(i[0])
    M.sort()
    for i in M:
        print(i)

solution()
        
