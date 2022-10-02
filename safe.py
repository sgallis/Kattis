#https://open.kattis.com/contests/xrjk7f/problems/safe

from collections import deque
import sys

def click(grid, i, j):
    gridbis = [x.copy() for x in grid]
    for k in range(3):
        gridbis[i][k] = (gridbis[i][k] + 1)%4
        if k != i:
            gridbis[k][j] = (gridbis[k][j] + 1)%4
    return gridbis

def solution():
    final_grid = [[0, 0, 0] for i in range(3)]
    grid = [list(map(int, line.split())) for line in sys.stdin]
    already = set()
    already.add(tuple(map(tuple,grid)))
    q = deque()
    q.append((grid, 0))
    while q != deque():
        grid, nb_moves = q.popleft()
        if grid == final_grid:
            print(nb_moves)
            return
        for i in range(3):
            for j in range(3):
                gridbis = click(grid, i, j)
                gridbis1 = tuple(map(tuple, gridbis))
                if gridbis1 not in already:
                    already.add(gridbis1)
                    q.append((gridbis, nb_moves + 1))
    print(-1)

solution()

