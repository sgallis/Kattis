#https://open.kattis.com/problems/groupthink

import sys

def solution():
    n = int(input())
    M = [[True]*n for i in range(n)]
    for line in sys.stdin:
        i, j, k = map(int, line.rstrip("\n").split())
        M[i][j] = k
    #print(M)
    # associativité
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if M[M[x][y]][z] != M[x][M[y][z]]:
                    print("magma")
                    return
    
    # élément neutre
    neutre = -8
    for i in range(n):
        #print(f"M[i]{M[i]}")
        #print(f"èl'autre{[M[x][i] for x in range(n)]}")
        if M[i] == [i for i in range(n)] and [M[x][i] for x in range(n)] == [i for i in range(n)]:
            neutre = i
        #print(neutre)
    if neutre == -8:
        print("semigroup")
        return
    # inverse
    a = False
    for x in range(n):
        for y in range(n):
            if M[x][y] == M[y][x] and M[x][y] == neutre:
                a = True
                break
        if not a:
            print("monoid")
            return
        a = False
    print("group")

solution()
