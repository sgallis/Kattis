#https://open.kattis.com/problems/different

import sys

def solution():
    a = list(map(int, input().split(" ")))
    while True:
        print(abs(a[0] - a[1]))
        try:
            a = list(map(int, input().split(" ")))
        except:
            sys.exit()
        

solution()