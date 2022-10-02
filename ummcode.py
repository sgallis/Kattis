#https://open.kattis.com/contests/bxmyat/problems/ummcode
import sys

def test_code(word):
    digits = [str(i) for i in range(0,10)]
    letters = [chr(i) for i in range(97 , ord("m"))]
    letters2 = [chr(i) for i in range(ord("m") + 1, ord("u"))]
    letters3 = [chr(i) for i in range(ord("u") + 1, 97+26)]
    for j in word:
        if j in digits or j in letters or j in letters2 or j in letters3:
            return False
    return True

def modify(word):
    s = ""
    for j in word:
        if j == "u":
            s = s + "1"
        else:
            s = s + "0"
    return s
def solution():
    sentence = list(input().split())
    L = []
    for i in sentence:
        if test_code(i):
            L.append(i)
    code = []
    for i in range(len(L)):
        word = L[i]
        w = ""
        for j in word:
            if j=="u" or j=="m":
                w = w + j
        code.append(w)
    for i,x in enumerate(code):
        code[i] = modify(x)
    i = 0
    sum = 0
    s = ""
    while i < len(code):
        s = s + code[i]
        if len(s) < 5:
            pass
        else:
            while len(s) > 6:
                inte = int(s[: 7], 2)
                sys.stdout.write(f"{chr(inte)}")
                s = s[7:]
            if len(s) >5:
                inte = int(s, 2)
                sys.stdout.write(f"{chr(inte)}")
                s = ""
        i += 1
        if i == len(code):
            while len(s) > 6:
                inte = int(s[: 7], 2)
                sys.stdout.write(f"{chr(inte)}")
                s = s[7:]
            if len(s) > 5:
                inte = int(s, 2)
                sys.stdout.write(f"{chr(inte)}")
                s = ""
solution()