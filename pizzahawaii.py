#https://open.kattis.com/problems/pizzahawaii


def test_1(d, L):
    for x in d:
        if len(d[x]) == 1 and x not in L:
            return x, list(d[x])[0]
    return False, False


def solution():
    for i in range(int(input())):
        if i != 0:
            print("\n")
        d = dict()
        setss = dict()
        for _ in range(int(input())):
            pizza = input()
            foreign = input().split()[1 :]
            english = input().split()[1 :]
            sforeign = {y for y in foreign}
            senglish = {y for y in english}
            setss.setdefault(pizza, [list(sforeign), list(senglish)])

            for x in foreign:
                d.setdefault(x, set())
                if d[x] == set():
                    d[x] = senglish 
                else:
                    d[x] = d[x].intersection(senglish)
        for x in d:
            for pizzaname in setss:
                if x not in setss[pizzaname][0]:
                    for z in setss[pizzaname][1]:
                        if z in d[x]:
                            d[x].remove(z)
        L = []
        t, truc = test_1(d, L)
        while t != False:
            for x in d:
                if len(d[x]) > 1:
                    for j in d[x]:
                        if j == truc:
                            d[x].remove(j)
            L.append(t)
            t, truc = test_1(d, L)
            i += 1     
        keys = list(d.keys())
        keys.sort()
        for x in keys:
            L = list(d[x])
            L.sort()
            for y in L:
                print(f"({x}, {y})")

solution()



            