#https://open.kattis.com/problems/unionfind
from sys import stdin

class UnionFind():
    def __init__(self, parent, size):
        self.parent = parent
        self.size = size

    """def MakeSet(self, a):
        if self.parent.get(a) == None:
            self.parent.setdefault(a, a)
            self.size.setdefault(a, 1)"""

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
    N ,Q = map(int, input().split())
    tree = UnionFind(list(range(N)), [1] * N)

    for line in stdin:
        command, a, b = line.split()
        if command == "=":
            tree.UnionSet(int(a), int(b))
        else:
            if tree.FindSet(int(a)) == tree.FindSet(int(b)):
                print("yes")
            else:
                print("no")

solution()




