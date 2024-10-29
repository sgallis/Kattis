#https://open.kattis.com/problems/telephones
import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    while N != 0 or M != 0:
        d = dict()
        for _ in range(N):
            L = list(map(int, sys.stdin.readline().split()))
            d.setdefault((L[0], L[1]), [L[2], L[2] + L[3]])
        
        for _ in range(M):
            L = list(map(int, sys.stdin.readline().split()))
            interval = [L[0], L[0] + L[1]]
            s = 0
            for i in d:
                if L[1] == 0:
                    pass
                elif (interval[0] >= d[i][0] and interval[0] < d[i][1]) or (interval[1] > d[i][0] and interval[1] < d[i][1]) or (interval[0] < d[i][0] and interval[1] >= d[i][1]):
                    s += 1
            sys.stdout.write(f"{s}\n")
        N, M = map(int, sys.stdin.readline().split())

solution()

