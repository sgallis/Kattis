# https://open.kattis.com/problems/longincsubseq

import sys
import bisect


def solution():
    for line in sys.stdin:
        L = line.split()
        if len(L) == 1:
            l = int(L[0])
        else:
            L = list(map(int, L))
            M = []
            P = [None]*(max(L)+1)
            K = 
            for i, x in enumerate(L):
                if i == 0:
                    M.append((x,i))
                else:             
                    ind = bisect.bisect_left(M, x)
                    M[ind] = x
                    if ind > 0:
                        P[x] = M[ind-1]

            sys.stdout.write(f"{len(index)}\n")
            sys.stdout.write(" ".join(map(str, index)) + "\n")
#store parent index in a tree
solution()
                
