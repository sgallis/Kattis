#https://open.kattis.com/problems/artichoke
from math import cos, sin

def solution():
    L = list(map(int, input().split()))
    p = L[0]
    a = L[1]
    b = L[2]
    c = L[3]
    d = L[4]
    n = L[5]
    stocks = []
    for k in range(1, n + 1):
        stocks.append(p * (sin(a * k + b) + cos(c * k + d) + 2))
    decline = 0
    maxdecline = 0
    maxvalue = stocks[0]
    minvalue = stocks[0]
    for k in range(len(stocks) - 1):
        if stocks[k] > stocks[k + 1]:
            if stocks[k + 1] < minvalue:               
                decline += minvalue - stocks[k + 1]
                minvalue = stocks[k + 1]
                if decline > maxdecline:
                    maxdecline = decline
        else:
            if stocks[k + 1] > maxvalue:
                maxvalue = stocks[k + 1]
                decline = 0
                minvalue = stocks[k + 1]
    print(maxdecline)
        
solution()

