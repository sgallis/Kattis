#https://open.kattis.com/problems/basicprogramming2


def solution():
    N, t = map(int, input().split())
    if t == 1:
        A = set(map(int, input().split()))
        for x in A:
            if 7777 - x in A:
                print("Yes")
                return
        print("No")
    elif t == 2:
        A = {}
        for x in list(map(int, input().split())):
            A.setdefault(x, 0)
            if A[x] == 1:
                print("Contains duplicate")
                return
            A[x] += 1
        print("Unique")
    elif t == 3:
        A = {}
        a = N / 2
        for x in list(map(int, input().split())):
            A.setdefault(x, 0)
            A[x] += 1
            if A[x] > a:
                print(x)
                return
        print(-1)
    elif t == 4:
        A = list(map(int, input().split()))
        A.sort()
        a = N % 2
        x = N // 2
        if a == 0:
            print(f"{A[x - 1]} {A[x]}")
        else:
            print(A[x])
    else:
        L = list(map(int, input().split()))
        L.sort()
        for x in L:
            if x >= 100 and x <= 999:
                print(x, end = " ")

solution()



