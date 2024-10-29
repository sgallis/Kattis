#https://open.kattis.com/problems/a1paper

def can(n, m, L):
    if n  >= len(L):
        return False
    else:
        if L[n] >= m:
            return True
        else:
            k = 2 * (m - L[n])
            return can(n + 1, k, L)
 
def length(n, m, L, format):
    if n >= len(L):
        return False
    else:
        if L[n] >= m:
            if m % 2 == 0:
                return (m // 2) *max(format[n])
            else:
                return (m // 2 + 1)* max(format[n])
        else:
            k = 2 * (m - L[n])
            if m % 2 == 0:
                return m // 2 * max(format[n]) + length(n + 1, k, L, format)
            else:
                return (m // 2 + 1)* max(format[n]) + length(n + 1, k, L, format)

def solution():
    n = int(input())
    sizes = [0, 0] + list(map(int, input().split()))
    if can(2, 2, sizes) == False:
        print("impossible")
    else:
        format = {0:[0,0]}
        for i, x in enumerate(sizes):
            if i != 0:
                if i == 1:
                    format.setdefault(i, [2**(-3/4 + 1), 2**(-5/4)])
                if i == 2:
                    format.setdefault(i, [2**(-3/4), 2**(-5/4)])
                else:
                    format.setdefault(i, [max(format[i - 1]) / 2, min(format[i - 1])])
        print(length(2, 2, sizes, format))


solution()