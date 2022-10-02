#https://open.kattis.com/problems/paintball
import sys

def solution():
    N, M = map(int, input().split())
    d = {i:[] for i in range(1, N + 1)}
    for _ in range(M):
        p1, p2 = map(int, input().split())
        d[p1].append(p2)
        d[p2].append(p1)
    
    
    
