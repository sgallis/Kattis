#https://open.kattis.com/problems/3dprinter


import math

def solution(n):
    return math.ceil(math.log(n, 2) + 1)


n = int(input())
print(solution(n))

#U_2^n = n puis passer à N imprimantes

