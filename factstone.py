#https://open.kattis.com/problems/factstone

import sys
from math import log

"""L = [3]
ln = log(2) + log(3)
bench = 3
bit = 4
for i in range(20):
    bit = bit * 2
    while ln + log(bench+1) <= bit*log(2):
        bench += 1
        ln += log(bench)
    L.append(bench)
print(L)"""

    

def solution():
    L = [3, 5, 8, 12, 20, 34, 57, 98, 170, 300, 536, 966, 1754, 3210, 5910, 10944, 20366, 38064, 71421, 134480, 254016]
    for line in sys.stdin:
        n = int(line.rstrip("\n"))
        if n == 0:
            return
        year = (n - 1960)//10
        sys.stdout.write(f"{L[year]}\n")

solution()
