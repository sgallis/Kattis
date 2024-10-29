#https://open.kattis.com/problems/tram


def solution():
    N = int(input())
    s = 0
    for i in range(N):
        L = list(map(int, input().split()))
        s += L[1] - L[0]
    return s / N
print(solution())