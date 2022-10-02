# https://open.kattis.com/problems/fallingapart/en

n = int(input())

L = list(map(int, input().split()))
L.sort()
L.reverse()

A = sum(L[::2])
B = sum(L) - A
print(A, B)
