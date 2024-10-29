#https://open.kattis.com/problems/sequence

def solution():
    N = int(input())
    L = [1]
    a = 1
    while 2 * a <= N:
        L.append(2 * a)
        a = 2 *a 
    print(len(L))
    print(" ".join(map(str, L)))

solution()