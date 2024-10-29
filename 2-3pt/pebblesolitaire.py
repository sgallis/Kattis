#https://open.kattis.com/problems/pebblesolitaire
from copy import deepcopy

def valid(L):
    moves = []
    for i in range(1, len(L) - 1):
        if L[i + 1] == "-" and L[i - 1] == "o" and L[i] == "o":
            moves.append([i - 1, i + 1])

        elif L[i + 1] == "o" and L[i - 1] == "-" and L[i] == "o":
            moves.append([i + 1, i - 1])
    return moves

def count_pebbles(L):
    s = 0
    for x in L:
        if x == "o":
            s += 1
    return s

def modify(L, x):
    K = deepcopy(L)
    K[x[0]] = "-"
    K[x[1]] = "o"
    K[max(x) - 1] = "-"
    return K

def graph(L):
    M = []
    if valid(L) == []:
        return L
    else:
        for x in valid(L):
            M = M + graph(modify(L, x))
        return M

def solution():
    n = int(input())
    for _ in range(n):
        board = [x for x in input()]
        grap = graph(board)
        s = 12
        for i, x in enumerate(grap):
            if i % 12 == 11:
                j = count_pebbles(grap[i - 11 : i + 1])
                if j < s:
                    s = j
        print(s)
    
solution()
