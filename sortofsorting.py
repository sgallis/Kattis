#https://open.kattis.com/problems/sortofsorting

def solution():
    z = 0
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            if z != 0:
                print("")
            L = {}
            M = {}
            L1 = []
            for i in range(n):
                a = input()
                x1, x2 = ord(a[0]), ord(a[1])      
                M.setdefault(x1, [])
                M[x1].append(x2)
                L.setdefault((x1, x2), [])
                L[(x1, x2)].append(a)
                if x1 not in L1:
                    L1.append(x1)
            L1.sort()
            for x in L1:
                L2 = sorted(set(M.get(x)))
                for y in L2:
                    for k in L.get((x,y)):
                        print(k)
            z += 1

solution()
print(type(set("abracadabra")))
print(set([0,1,1,2,3,5,5]))
            

                

