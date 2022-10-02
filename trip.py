#https://open.kattis.com/problems/trip

def solution():
    n = int(input())
    while n != 0:
        L = []
        for i in range(n):
            L.append(float(eval(input())))
        L.sort()
        m = sum(L) / len(L)
        s = 0
        i = 0
        while L[i] <= m:
            i += 1
        for j in L[i :]:
            s += j - m
        print(f"${s}")
        n = int(input())

solution()