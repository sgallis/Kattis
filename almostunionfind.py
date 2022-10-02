#https://open.kattis.com/problems/almostunionfind

import sys

class UnionFind():
    def __init__(self, parent, size):
        self.parent = parent
        self.size = size

    def FindSet(self, a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.FindSet(self.parent[a])
            return self.parent[a]

    def UnionSet(self, a, b):
        a = self.FindSet(a)
        b = self.FindSet(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a 
            self.parent[b] = a
            self.size[a] += self.size[b]
    
    def Move(self, p, q):
        a = self.FindSet(p)
        b = self.FindSet(q)
        if a != b:
            self.parent[p] = b
            self.size[b] += 1
            self.size[a] -= 1

def solution():
    n, m = map(int, input().split())
    countm = 0
    disjointSet = UnionFind([i for i in range(n + 1)], [1 for i in range(n + 1)])
    for line in sys.stdin:
        if countm < m:
            commands = list(map(int, line.split()))
            countm += 1
            if commands[0] == 1:
                disjointSet.UnionSet(commands[1], commands[2])
            elif commands[0] == 2:
                disjointSet.Move(commands[1], commands[2])
            else:
                parent = disjointSet.FindSet(commands[1])
                sys.stdout.write(f"{disjointSet.size[disjointSet.FindSet(commands[1])]} {sum([i for i in range(n + 1) if disjointSet.FindSet(i) == parent])}\n")
        else:
            n, m = map(int, sys.stdin.readline().split())
            countm = 0
            disjointSet = UnionFind([i for i in range(n + 1)], [1 for i in range(n + 1)])

solution()
