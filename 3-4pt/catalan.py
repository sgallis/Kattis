#https://open.kattis.com/problems/catalan

import sys

def solution():
    k = input()
    for line in sys.stdin:
        n = int(line)
        if n <= 1:
            sys.stdout.write("1\n")
        else:
            p = 1
            q = 1
            for i in range(2, n + 1):
                p = p * (n+i)
                q = q*i
            sys.stdout.write(f"{p//q}\n")


solution()
