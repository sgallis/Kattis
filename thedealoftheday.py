#https://open.kattis.com/problems/thedealoftheday
from math import factorial

def solution(M, number):
    L = []
    for i, j in enumerate(M):
        if j != 0:
            L.append(j)
    if number > len(L):
        return 0
    elif number == len(L):
        p = 1
        for i in L:
            p = p * i
        return p
    elif number == 1:
        return sum(L)
    else:
        return solution(L[:-1], number) + solution(L[:-1], number - 1) * L[-1]
        
def binom(n, p):
    return factorial(n)/(factorial(p)*factorial(n-p))


print(solution(list(map(int, input().split())), number = int(input())))


