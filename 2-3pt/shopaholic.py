#https://open.kattis.com/problems/shopaholic

def solution():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    L.reverse()
    discount = 0
    for i in range(2, len(L), 3):
        discount += L[i]

    print(discount)

solution()


