#https://open.kattis.com/problems/virtualfriends
import sys

class UnionFind():
    def __init__(self, parent, size):
        self.parent = parent
        self.size = size

    def MakeSet(self, a):
        if self.parent.get(a) == None:
            self.parent.setdefault(a, a)
            self.size.setdefault(a, 1)

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

def solution():
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        N = int(sys.stdin.readline())
        connections = UnionFind(dict(), dict())
        for j in range(N):
            command = sys.stdin.readline()
            A, B = command.split()
            connections.MakeSet(A)
            connections.MakeSet(B)
            connections.UnionSet(A, B)
            sys.stdout.write(f"{connections.size[connections.FindSet(A)]}\n")

solution()