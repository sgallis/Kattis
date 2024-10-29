#https://open.kattis.com/problems/alexandbarb




def solution():
    k, m, n = map(int, input().split())
    if k // (m + n) * (m + n) + m > k:
        print("Barb")
    else:
        print("Alex")

solution()