#https://open.kattis.com/problems/basicremains
import sys

def solution():
    L = sys.stdin.readline()
    while L != "0":
        try : 
            b, p, m = L.split()
        except:
            return
        b = int(b)
        reste = int(p, b) % int(m, b)
        i = 1
        sum = ""
        if reste == 0:
            print(0)
        else:
            while reste != 0:
                r = reste % (b ** i)
                reste -= r 
                r = r // b ** (i-1)
                sum = str(r) + sum
                i += 1
            print(sum)
        L = sys.stdin.readline()
            

solution()
