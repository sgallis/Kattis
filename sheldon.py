# https://open.kattis.com/contests/v6h3f6/problems/sheldon
from math import log,floor

X, Y = map(int, input().split())

occ = 0
if X == 0 and Y > 0:
    X += 1
    a, b = floor(log(X,2))+1, floor(log(Y,2))+2
elif X == 0 and Y == 0:
    a,b=0,0
else:
    a, b = floor(log(X,2))+1, floor(log(Y,2))+2
    
for puissance in range(a,b):
    if puissance == 1:
        occ += 1
    for N in range(1, puissance):
        for M in range(0, puissance):
            if N+M <= puissance:
                q,r = puissance//(N+M), puissance % (N+M)
                L = [1 for i in range(N)]+[0 for i in range(M)]
                L = L*q + [1 for i in range(N)]*r
                if not L:
                    pass
                elif (r == 0 or r==N):
                    k = int(''.join(map(str, L)),2)
                    if k >=X and k <=Y:
                        occ += 1

print(occ)