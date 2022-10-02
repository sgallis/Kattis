# https://open.kattis.com/contests/btb6v7/problems/moneymatters

n, m = map(int,input().split())

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

money = []
for _ in range(n):
    money.append(int(input()))

tree = UnionFind([i for i in range(n)],[1 for _ in range(n)])
for _ in range(m):
    tree.UnionSet(*map(int,input().split()))


possible = True
parents = []
for x in tree.parent:
    k = tree.FindSet(x)
    if k not in parents:
        parents.append(k)

for x in parents:
    s = 0
    for i in range(n):
        if tree.FindSet(i) == x:
            s += money[i]
    if s != 0:
        possible = False
        break
if possible:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

    



