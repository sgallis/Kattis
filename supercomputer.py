#https://open.kattis.com/contests/xrjk7f/problems/supercomputer

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
    N, K = map(int, input().split())
    memory = FenwickTree(N + 1)
    for line in sys.stdin:
        L = line.split()
        if line[0] == "F":
            i = int(L[1])
            if memory.sum(i + 1) - memory.sum(i) == 1:
                memory.update(i, -1)
            else:
                memory.update(i, 1)

        else:
            sys.stdout.write(f"{memory.sum(int(L[2]) + 1) - memory.sum(int(L[1]))}\n")

solution()