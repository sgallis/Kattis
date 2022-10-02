#https://open.kattis.com/problems/falling

from math import sqrt

def diviseurs(D):
    div = set()
    for i in range(1, int(sqrt(D)) + 1):
        if D % i == 0:
            div.add(i)
            div.add(D//i)
    return div

def solution():
    D = int(input())
    div = diviseurs(D)
    m = max(div)
    for s in div:
        for d in div:
            if s * d == D:
                if s - d <= 0:
                    s, d = d, s
                #print(f"{s} {d}")
                if (s-d)%2==0 and (s+d)%2==0:
                    print(f"{(s-d)//2} {(s+d)//2}")
                    return        
    print("impossible")


solution()
    