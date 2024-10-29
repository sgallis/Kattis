# https://open.kattis.com/contests/v6h3f6/problems/dicecup


d= dict()
N, M = map(int, input().split())

for i in range(1, N + 1):
    for m in range(1, M + 1):
        d.setdefault(i+m,0)
        d[i+m] += 1

a = max(d.values())
L = []
for j in d:
    if d[j] == a:
        L.append(j)
L.sort()

for j in L:
    print(j)