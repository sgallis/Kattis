#https://open.kattis.com/problems/catalansquare

def solution():
    s = 0
    n = int(input())
    L = {}
    for j in range(n + 1):
        if j == 0:
            L.setdefault(0, 1)
        else:
            L.setdefault(j, L[j - 1] * 2 * (2 * j - 1) // (j + 1))
    for i in range(n + 1):
        s += L[i] * L[n - i]
    print(s)

solution()
        
    