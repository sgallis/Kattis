#https://open.kattis.com/problems/froshweek
import sys

def solution():
    n = int(input())
    d = dict()
    i = 0
    for _ in range(n):
        d.setdefault(int(sys.stdin.readline()), i)
        i += 1
    swaps = 0
    while len(d) > 1:
        a = max(d)
        ind = d.pop(a)
        for x in d:
            if d.get(x) > ind:
                d[x] -= 1
        swaps += len(d) - ind

    print(swaps)

solution()
