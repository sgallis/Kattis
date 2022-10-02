#https://open.kattis.com/problems/pathtracing

def solution():
    L = [["S"]]
    i = [0, 0]
    while True:
        try:
            command = input()
        except:
            L[i[0]][i[1]] = "E"
            l = len(L[0])
            h = len(L)
            for j in range(l + 2):
                if j != l + 1:
                    print("#", end = "")
                else:
                    print("#")
            for y in L:
                for j, x in enumerate(y):
                    if j == 0:
                        print("#", end = "")
                    print(x, end = "")
                    if j == len(L):
                        print("#")
            for j in range(l + 2):
                print("#", end = "")
            return
        if command == "down":
            if i[0] == len(L) - 1:
                L.append([" " for i in range(len(L[0]))])
                i[0] += 1
                if L[i[0]][i[1]] != "S":
                    L[i[0]][i[1]] = "*"
            else:
                i[0] += 1
                if L[i[0]][i[1]] != "S":
                    L[i[0]][i[1]] = "*"
        elif command == "right":
            if i[1] == len(L[0]) - 1:
                for j in range(len(L)):
                    L[j].append(" ")
                i[1] += 1
                if L[i[0]][i[1]] != "S":
                    L[i[0]][i[1]] = "*"
            else:
                i[1] += 1
                if L[i[0]][i[1]] != "S":
                    L[i[0]][i[1]] = "*"
        elif command == "up":
            if i[0] == 0:
                L = [[" " for i in range(len(L[0]))]] + L
                if L[i[0]][i[1]] != "S":
                    L[[0]][i[1]] = "*"
            else:
                i[0] -= 1
                if L[i[0]][i[1]] != "S":
                    L[i[0]][i[1]] = "*"
        else:
            if i[1] == 0:
                for j in range(len(L)):
                    L[j] = [" "] + L[j]
                if L[i[0]][i[1]] != "S":
                    L[i[0]][i[1]] = "*"
            else:
                i[1] -= 1
                if L[i[0]][i[1]] != "S":
                    L[i[0]][i[1]] = "*"
solution()





