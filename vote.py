#https://open.kattis.com/problems/vote

def solution():
    for i in range(1, int(input()) + 1):
        nb = int(input())
        s = 0
        max = 0
        M = []
        for j in range(nb):
            candidat = int(input())
            if candidat > max:
                max = candidat
            s += candidat
            M.append(candidat)
        L = []
        for i, x in enumerate(M):
            if x == max:
                L.append([i + 1, x])
        if len(L) >= 2:
            print("no winner")
        else:
            if L[0][1] > s/2:
                print(f"majority winner {L[0][0]}")
            else:
                print(f"minority winner {L[0][0]}")

solution()

