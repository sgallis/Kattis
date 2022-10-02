#https://open.kattis.com/problems/secretsanta

def solution(): #pn = (1 - 1 / n) + 1 / n
    s = 0
    n = int(input())
    if n == 1:
        return 1
    else:
        for j in range(2, n + 1):
            s = (1 - 1 / j) * s + 1 / j
    print(s)
solution()