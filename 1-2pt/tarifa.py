#https://open.kattis.com/problems/tarifa

def solution():
    X = int(input())
    N = int(input())
    X = X * (N + 1)
    for i in range(N):
        X -= int(input())
    print(X)

solution()