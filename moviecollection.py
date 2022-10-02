#https://open.kattis.com/contests/xrjk7f/problems/moviecollection

import sys

class FenwickTree():
    def __init__(self, n):
        self.L = [0] * (n + 1)
        self.size = n + 1
    
    def update(self, i, diff):
        i += 1
        while i < self.size:
            self.L[i] += diff
            i += i & -i
    
    def sum(self, i):# on ne prend pas en compte l'indice i
        result = 0
        while i > 0:
            result += self.L[i]
            i = i & (i- 1)
        return result

def solution():
    n = int(input())
    for _ in range(n):
        movies, requests = map(int, sys.stdin.readline().split())
        want = list(map(int, sys.stdin.readline.split()))
        stack = FenwickTree(movies)
        for j in range(movies):
            stack.update(j, 1)
        for i in want:
            ind = i - 1
            sys.stdout.write(f"{stack.sum(ind + 1)}")
            stack.update(ind , sum(stack.size - 1)
        
