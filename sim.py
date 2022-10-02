#https://open.kattis.com/problems/sim

def solution():
    n = int(input())
    for i in range(n):
        command = input()
        s = ""
        i = 0
        for x in command:
            if x == "<":
                if i == 0:
                    pass
                elif i == len(s):
                    s = s[: -1]
                    i -= 1
                else:
                    s = s[: i - 1] + s[i :]
                    i -= 1
            elif x == "[":
                i = 0
            elif x == "]":
                i = len(s)
            else:
                if i == len(s):
                    s += x
                    i += 1
                else:
                    s = s[: i] + x + s[i :]
                    i += 1
        print(s)

solution()


