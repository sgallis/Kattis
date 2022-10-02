#https://open.kattis.com/problems/akcija

def solution():
    n = int(input())
    L = []
    for i in range(n):
        L.append(int(input()))
    L.sort()
    l = len(L)
    q = l // 3
    r = l % 3
    s = 0
    for j in range(r, 3 * q , 3):
        s += L[j + 1] + L[j + 2]
    if r == 1:
        s += L[0]
    elif r == 2:
        s += L[0] + L[1]
    print(s)
solution()
