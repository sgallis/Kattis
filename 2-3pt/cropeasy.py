#https://open.kattis.com/problems/cropeasy

import sys

def center(p1, p2, p3):
    return (p1[0] + p2[0] + p3[0])%3 == 0 and (p1[1] + p2[1] + p3[1])%3 == 0

def solution():
    T = int(input())
    case = 1
    for line in sys.stdin:
        s = 0
        n, A, B, C, D, x0, y0, M = map(int, line.split())
        trees = [(x0, y0)]
        for i in range(0, n - 1):
            input0 = ((A * trees[i][0] + B)%M, (C * trees[i][1] + D)%M)
            trees.append(input0)
            used1 = []
            if len(trees) >= 3:
                for j in trees[:-1]:
                    used1.append(j)
                    for l in trees[:-1]:
                        if l not in used1:
                            if center(input0, j, l):
                                s += 1
        sys.stdout.write(f"Case #{case}: {s}\n")
        case += 1

solution()
    
