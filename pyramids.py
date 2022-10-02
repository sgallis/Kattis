#https://open.kattis.com/problems/pyramids

def solution():
    n = int(input())
    s = 0
    while n >= 0:
        s += 1
        n -= (2 * s - 1) ** 2
    print(s - 1)

solution()