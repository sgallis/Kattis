#https://open.kattis.com/problems/armystrengtheasy

def solution():
    n = int(input())
    for _ in range(n):
        blank = input()
        n,g = map(int,input().split())
        maxg = max(list(map(int, input().split())))
        maxm = max(list(map(int, input().split())))
        if maxg >= maxm:
            print("Godzilla")
        else:
            print("MechaGodzilla")

solution()