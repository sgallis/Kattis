#https://open.kattis.com/contests/bxmyat/problems/tildes
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
    n, m = map(int, input().split())
    groups = UnionFind(dict(), dict())
    for i in range(1, n + 1):
        groups.MakeSet(i)
    for line in sys.stdin:
        a = line.split()
        if line[0] == "t":
            groups.UnionSet(int(a[1]), int(a[2]))
        else:
            sys.stdout.write(f"{groups.size[groups.FindSet(int(a[1]))]}\n")

solution()