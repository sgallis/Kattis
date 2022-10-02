# https://open.kattis.com/contests/pzmq28/problems/deceptivedirections

from collections import deque

w,h = map(int, input().split())
carte = [input() for _ in range(h)]
command = input()
l = len(command)
dup = [[] for _ in range(l+1)]
found = dict()
fault = []
carte2 = [[j for j in i] for i in carte]
# parcours de graphe

for y in range(h):
    for x in range(w):
        if carte[y][x] == "S":
            Sx, Sy = x, y

# parcours en largeur

stack = deque([(Sx, Sy, 0, True)])

while stack:
    nod = stack.popleft()
    print(nod)
    next = nod[2] + 1
    next_poss = []
    if nod in dup[nod[2]]:
        pass
    elif next > l+1:
        pass
    elif next == l+1:
        if nod[0]>=0 and nod[0] < w and nod[1] >= 0 and nod[1] < h and carte[nod[1]][nod[0]] == ".":
            found.setdefault((nod[0],nod[1]),0)
            found[(nod[0],nod[1])] += 1
    elif command[nod[2]] == "N":
        next_poss.append((nod[0], nod[1] + 1, next)) # sud
        next_poss.append((nod[0] + 1, nod[1], next)) # est
        next_poss.append((nod[0] - 1, nod[1], next)) # ouest
    elif command[nod[2]] == "S":
        next_poss.append((nod[0], nod[1] - 1, next)) # nord
        next_poss.append((nod[0] + 1, nod[1], next)) # est
        next_poss.append((nod[0] - 1, nod[1], next)) # ouest
    elif command[nod[2]] == "W":
        next_poss.append((nod[0], nod[1] + 1, next)) # sud
        next_poss.append((nod[0] + 1, nod[1], next)) # est
        next_poss.append((nod[0], nod[1] - 1, next)) # nord
    else:
        next_poss.append((nod[0], nod[1] + 1, next)) # sud
        next_poss.append((nod[0], nod[1] - 1, next)) # nord
        next_poss.append((nod[0] - 1, nod[1], next)) # ouest

    for j in next_poss:
        if j not in stack and j not in dup[j[2]]:
            stack.append(j)
        elif j in stack:
            dup[j[2]].append(j)
        


for k in found:
    if found[k] <= 1:
        carte2[k[1]][k[0]] = "!"

for i in carte2:
    print("".join(i))



