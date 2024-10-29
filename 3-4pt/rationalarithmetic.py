#https://open.kattis.com/problems/rationalarithmetic

import sys
from math import gcd

def solution():
    n = int(input())
    for line in sys.stdin:
        L = line.split()
        x1 = int(L[0])
        y1 = int(L[1])
        op = L[2]
        x2 = int(L[3])
        y2 = int(L[4])
        if op == "+":
            p = x1 * y2 + x2 * y1
            q = y1 * y2
            pgcd = abs(gcd(p, q))
            p = p // pgcd
            q = q // pgcd
            
        elif op == "-":
            p = x1 * y2 - x2 * y1
            q = y1 * y2
            pgcd = abs(gcd(p, q))
            p = p // pgcd
            q = q // pgcd
            
        elif op == "*":
            p = x1 * x2
            q = y1 * y2
            pgcd = abs(gcd(p, q))
            p = p // pgcd
            q = q // pgcd
            
        else:
            p = x1 * y2
            q = y1 * x2
            pgcd = abs(gcd(p, q))
            p = p // pgcd
            q = q // pgcd
        if q < 0:
            p = -p
            q = abs(q)
        sys.stdout.write(f"{p} / {q}\n")

solution()
