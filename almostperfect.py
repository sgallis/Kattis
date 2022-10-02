#https://open.kattis.com/problems/almostperfect
from math import sqrt
import sys
def test(n):
    s = 0
    for i in range(1,int(sqrt(n)) + 1):
        if n % i == 0:
            if i == 1 and n != 1:
                s += 1
            else:
                s += i
                if i < sqrt(n):
                    s += n // i
        if s > n + 2:
            return(f"{n} not perfect")
    if s==n:
        return(f"{n} perfect")
    elif s >= n -2 and s <= n + 2:
        return(f"{n} almost perfect")
    else:
        return(f"{n} not perfect")



if __name__ == '__main__':
    while True:
        try:
            print(test(int(input())))
        except:
            sys.exit()
        
