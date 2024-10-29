#https://open.kattis.com/problems/trik

def solution():
    word = input()
    l = "A"
    for x in word:
        if x == "A":
            if l == "A":
                l = "B"
            elif l == "B":
                l = "A"
        elif x == "B":
            if l == "B":
                l = "C"
            elif l == "C":
                l = "B"
        else:
            if l == "A":
                l = "C"
            elif l == "C":
                l = "A"
    if l == "A":
        print(1)
    elif l == "B":
        print(2)
    else:
        print(3)

solution()