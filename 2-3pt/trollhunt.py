#https://open.kattis.com/problems/trollhunt
from math import ceil
def solution():
    b, k, g = map(int, input().split())
    l = k // g
    print(ceil((b-1)/l) )

solution()