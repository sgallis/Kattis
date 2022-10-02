# https://open.kattis.com/contests/v6h3f6/problems/canvas

T = int(input())

def resol(L, N):
    if len(L) == 2:
        return sum(L)
    elif len(L) == 1:
        return 0
    else:
        if N//2 == N/2:
            return resol(L[:N//2], N//2) + resol(L[N//2:], N-N//2) + sum(L)
        else:
            return resol(L[:N//2 + 1], N//2+1) + resol(L[N//2+1:], N-N//2-1) + sum(L)

for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    print(resol(L,N))