#https://open.kattis.com/contests/bxmyat/problems/heirsdilemma


def divisible(i):
    L = [j for j in str(i)]
    for j in L:
        if i % int(j) != 0:
            return False
    return True

def different(i):
    L = [j for j in str(i)]
    L1 = list(set(L))
    L1.sort()
    L.sort()
    return L == L1

def zeros(i):
    return"0" in [j for j in str(i)]
       
def solution():
    L, H = map(int, input().split())
    s = 0
    for i in range(L, H + 1):
        if not zeros(i):
            if different(i) and divisible(i):
                s+=1

    print(s)
solution()