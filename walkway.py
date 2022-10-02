#https://open.kattis.com/problems/walkway

import sys

def area(L):
    a, b, h = L
    return (b - a/2)*h + 2 * a/2*h


def solution():
    for line in sys.stdin:
        L = line.split()
        if L == ["0"]:
            return
        elif len(L) == 1:
            n = int(L[0])
            M = []
        elif len(L) == 2:
            back = int(L[0])
            gazebo = int(L[1])
        else:
            L.append(area(L))
            M.append(list(map(int, L)))
        if back == gazebo:
            sys.stdout.write("0\n")
        

