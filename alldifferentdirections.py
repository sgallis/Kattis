#https://open.kattis.com/problems/alldifferentdirections
from math import sin, cos, sqrt, radians

def solution():
    n = int(input())
    while n != 0:
        xdestinations = []
        ydestinations = []
        for i in range(n):
            L = list(input().split(" "))
            directions = L[2: ]
            coordinates = [float(L[0]), float(L[1]), 0]
            for i in range(0, len(directions), 2):
                if directions[i] == "start":
                    coordinates[2] = float(directions[i + 1])
                elif directions[i] == "walk":
                    coordinates[0] += float(directions[i + 1]) * cos(radians(coordinates[2]))
                    coordinates[1] += float(directions[i + 1]) * sin(radians(coordinates[2]))
                elif directions[i] == "turn":
                    coordinates[2] += float(directions[i + 1])
            xdestinations.append(coordinates[0])
            ydestinations.append(coordinates[1])
        x = sum(xdestinations) / len(xdestinations)
        y = sum(ydestinations) / len(ydestinations)
        max = 0
        for j in range(len(xdestinations)):
            a = sqrt((xdestinations[j] - x) ** 2 + (ydestinations[j] - y) ** 2)
            if a > max:
                max = a
        print("{:.6f} {:.6f} {:.6f}".format(x, y, max))       
        n = int(input())
    

solution()
            
