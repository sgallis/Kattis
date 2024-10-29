#https://open.kattis.com/problems/parsinghex
import sys

def solution():
    for line in sys.stdin:
        s = ""
        i = 0
        l = len(line)
        j = False
        while i < l:
            if j:
                j = False
            elif i < l- 1 and ((line[i] == "0" and line[i + 1] == "x") or (line[i] == "0" and line[i + 1] == "X")):
                if s != "":
                    print(f"{s} {int(s, 16)}")
                s = line[i] + line[i + 1]
                j = True
            elif len(s) == 10:
                print(f"{s} {int(s, 16)}")
                s = ""
            elif line[i] not in [chr(x) for x in range(65, 71)] + [chr(x) for x in range(97, 103)] + [str(x) for x in range(0,10)]:
                if s != "":
                    print(f"{s} {int(s, 16)}")
                s = ""
            elif s[0:2] == "0x" or s[0:2] == "0X":
                s += line[i]
            i += 1
        if s!= "":
            print(f"{s} {int(s, 16)}")

solution()