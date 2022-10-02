#https://open.kattis.com/problems/qaly

def solution():
    s = 0
    for i in range(int(input())):
        L = list(map(float, input().split()))
        s += L[0] * L[1]
    print(s)

solution()
