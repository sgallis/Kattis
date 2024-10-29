#https://open.kattis.com/problems/babelfish

def solution():
    d = dict()
    a = input()
    while a != "":
        L = a.split()
        d.setdefault(L[1], L[0])
        a = input()
    while True:
        try:
            word = input().split()
            if d.get(word[0]) != None:
                print(d.get(word[0]))
            else:
                print("eh")
        except:
            break

solution()