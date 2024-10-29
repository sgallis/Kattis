# https://open.kattis.com/contests/btb6v7/problems/candlebox

D = int(input())
R = int(input())
T = int(input())

for rita in range(4,101):
    if rita-D >= 3:
        Rth = rita*(rita+1)//2 - 6
        Tth = (rita-D)*(rita-D+1)//2 -3
        if abs(Rth-R) == abs(Tth - T):
            print(abs(Rth-R))
            break
