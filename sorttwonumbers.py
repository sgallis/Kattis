#https://open.kattis.com/problems/sorttwonumbers

def solution():
    L = list(map(int, input().split()))
    L.sort()
    print(f"{L[0]} {L[1]}")
solution()