#https://open.kattis.com/problems/ignore

def test(x):
    for i in x: 
        if int(i) not in [0, 1, 2, 5, 6, 8, 9]:
            return False
    return True

def solution():
    L = [0, 1, 2, 5, 8]
    while True:
        try:
            n = int(input())
        except:
            return
        i = 0
        j = 0       
        while i < n:
            j += 1
            if test(str(j)):
                i += 1
        s = ""
        for x in str(j):
            r = int(x)
            if x == "0" or x == "1" or x == "5" or x == "8" or x == "2":
                s = x + s
            elif x == "6":
                s = "9" + s
            else:
                s = "6" + s

        print(s)

solution()

"""def solution():
    L = ["0", "1", "2", "5", "6", "8", "9"]
    d = {}
    i = 0
    j = 0
    while True:
        try:
            n = int(input())
        except:
            return
        if n in d:
            print(d[n])
        else:           
            while i < n:
                j += 1
                if test(str(j)):
                    i += 1
                    s = ""
                    for x in str(j)[ : : -1]:
                        if x == "0" or x == "1" or x == "5" or x == "8" or x == "2":
                            s += x
                        elif x == "6":
                            s += "9"
                        else:
                            s += "6"
                    d.setdefault(i, s)
            print(d[n])"""
            
