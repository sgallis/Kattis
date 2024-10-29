# https://open.kattis.com/problems/polymul1

import sys

T = int(input())

for _ in range(T):
    n1 = int(sys.stdin.readline())
    coeffs1 = list(map(int, sys.stdin.readline().rstrip().split()))
    n2 = int(sys.stdin.readline())
    coeffs2 = list(map(int, sys.stdin.readline().rstrip().split()))

    sys.stdout.write(f"{n1+n2}\n")

    coeffs = []
    for k in range(n1 + n2 + 1):
        s = 0
        for i in range(k + 1):
            j = k- i
            if j <= n2 and i <= n1:
                s += coeffs1[i] * coeffs2[j]
        coeffs.append(str(s))

    sys.stdout.write(" ".join(coeffs) + "\n")