#https://open.kattis.com/problems/logo

import sys
from math import radians, cos, sin, hypot

def solution():
    for _ in range(int(input())):
        coordinates = [0, 0]
        angle = 0 #en degrés
        for j in range(int(input())):
            line = sys.stdin.readline().split()
            if line[0] == "fd":
                coordinates[0] += float(line[1]) * cos(radians(angle))
                coordinates[1] += float(line[1]) * sin(radians(angle))
            elif line[0] == "lt":
                angle += float(line[1])
            elif line[0] == "bk":
                coordinates[0] -= float(line[1]) * cos(radians(angle))
                coordinates[1] -= float(line[1]) * sin(radians(angle))
            else:
                angle -= float(line[1])
        sys.stdout.write(f"{round(hypot(coordinates[0], coordinates[1]))}\n")


solution()