#https://open.kattis.com/problems/shatteredcake

def solution():
    w = int(input())
    n = int(input())
    s = 0
    for i in range(n):
        L = list(map(int, input().split()))
        s += L[0] * L[1]
    print(s // w)

solution()
