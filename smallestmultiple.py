#https://open.kattis.com/problems/smallestmultiple

import sys
from math import gcd

def ppcm(a,b):
    return a*b//gcd(a,b)

for line in sys.stdin:
    a = list(map(int, line.rstrip("\n").split()))
    pppcm = 1
    for i in range(len(a)):
        pppcm = ppcm(pppcm, a[i])
    sys.stdout.write(f"{pppcm}\n")
