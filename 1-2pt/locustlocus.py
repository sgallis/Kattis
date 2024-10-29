from math import gcd

k = int(input())
years = 0

for i in range(k):
    year, a, b = map(int, input().split())
    y = a*b//gcd(a,b)+year
    if years == 0:
        years = y
    elif years > y:
        years = y

print(years)
