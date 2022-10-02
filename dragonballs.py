# https://open.kattis.com/problems/dragonballs

from math import sqrt

n = int(input())
found = 0
def loop(x, y):
    global found
    global n
    print(f"{x} {y}", flush=True)
    d = int(input())
    if d == 0:
        found += 1
    if found == n:
        exit(0)
    return d


def solution():
    global found
    global n
    while found < n:
        y1, y2 = 0, 10**6
        # dichotomie
        while y1 < y2:
            dist = y2 - y1
            d1 = loop(0, y1 + dist//3)
            d2 = loop(0, y2-dist//3)
            if d1 <= d2:
                y2 -= dist//3 + 1
            else:
                y1 += dist//3 + 1
        # on cherche x
        x = loop(0, y1)
        loop(round(sqrt(x)), y1)


solution()
