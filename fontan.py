# https://open.kattis.com/contests/btb6v7/problems/fontan

import sys

N, M = map(int, input().split())

matrice = [list(input()) for _ in range(N)]
matrice_update = matrice.copy()


for _ in range(N*N):
    matrice = matrice_update.copy()

    for i in range(N):
        for j in range(M):
            if matrice[i][j] == "V":
                if i+1 < N:
                    if matrice[i+1][j] == ".":
                        matrice_update[i+1][j] = "V"
                    elif matrice[i+1][j] == "#":
                        if j + 1 < M and matrice_update[i][j+1] == ".":
                            matrice_update[i][j+1] = "V"
                        if j-1 >= 0 and matrice_update[i][j-1] == ".":
                            matrice_update[i][j-1] = "V"

for i in range(N):
    for j in range(M):
        sys.stdout.write(f"{matrice_update[i][j]}")
    sys.stdout.write("\n")

