# https://open.kattis.com/contests/btb6v7/problems/grapevine

import sys

n, m, d = map(int, input().split())

scepticism = list()
people = dict()

for i in range(n):
    person, lvl = sys.stdin.readline().rstrip().split()
    lvl = int(lvl)
    people[person] = lvl
    scepticism.append(lvl)

relations = [[] for _ in range(n)]

for _ in range(m):
    name1, name2 = sys.stdin.readline().rstrip().split()
    relations[people[name1]].append(people[name2])
    relations[people[name2]].append(people[name1])

origin = people[input()]
know1 = set([origin])
know2 = set([origin])

for _ in range(d):
    temp = []
    
    for i in know1:
        for k in relations[i]:
            know2.add(k)
            scepticism[k] -= 1
            if scepticism[k] == 0:
                temp.append(k)
    for j in temp:
        know1.add(j)
    if len(know2) == n:
        break

print(len(know2)-1)

    

