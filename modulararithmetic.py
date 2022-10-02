#https://open.kattis.com/problems/modulararithmetic

import sys
from math import gcd

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def solution():
    n, t = map(int, sys.stdin.readline().split())
    while (n,t) != (0, 0):
        for _ in range(t):
            L = list(sys.stdin.readline().split())
            a, b, op = int(L[0]), int(L[2]), L[1]
            if op == "+":
                sys.stdout.write(f"{(a%n + b%n)%n}\n")
            elif op == "*":
                sys.stdout.write(f"{(a%n * b%n)%n}\n")
            elif op == "-":
                sys.stdout.write(f"{(a%n - b%n)%n}\n")
            else:
                if b == 0:
                    sys.stdout.write(f"-1\n")
                elif gcd(b, n) != 1:
                    sys.stdout.write(f"-1\n")
                else:
                    sys.stdout.write(f"{(a%n * modinv(b, n))%n}\n")

        n ,t = map(int, sys.stdin.readline().split())

solution()