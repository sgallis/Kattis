#https://open.kattis.com/problems/persistent

import sys

def solution():
    for line in sys.stdin:
        n = int(line)
        L = []
        if n == -1:
            return
        elif n < 10:
            sys.stdout.write(f"1{n}\n")
        else:
            for i in list(range(2,10))[::-1]:
                while n % i == 0:
                    n = n//i
                    L.append(i)
            if n == 1:
                sys.stdout.write("".join(map(str, L[::-1])) + "\n")
            else:
                sys.stdout.write("There is no such number.\n")

solution()
