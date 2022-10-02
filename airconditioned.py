#https://open.kattis.com/problems/airconditioned

"""def rooms(n, temperatures):
    if n == 1:
        return 1
    else:
        L = temperatures[-1]
        for i in L:
            for j in temperatures[:-1]:
                if i in j:
                    return rooms(n - 1, temperatures[: -1])
        return rooms(n - 1, temperatures[ : -1]) + 1"""


def solution():
    n = int(input())
    temperatures = [list(map(int, input().split())) for i in range(n)]

    temperatures1 = [list(range(temperatures[i][0], temperatures[i][1] + 1)) for i in range(n)]
    d = {}
    for i in temperatures1:
        for j in i:
            d.setdefault(j, 0)
            d[j] = d[j] + 1
    val = sorted(d.values())
    lv = len(val)
    for i in range(0, lv):
        a = val[lv - 1 - i]
        M = list(d.keys())
        for j in M:
            if d[j] == a:
                
                


        
        
solution()