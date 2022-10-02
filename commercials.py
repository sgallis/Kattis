#https://open.kattis.com/problems/commercials

def max_sum(L):
    max_profit = L[0]
    profit_so_far = L[0]
    for x in L[1:]:
        profit_so_far = max(profit_so_far+x, x)
        max_profit = max(profit_so_far, max_profit)
    return max_profit

    



N, P = map(int, input().split())

def convertir(n):
    global P
    return int(n) - P

L = list(map(convertir, input().split()))
print(max_sum(L))


