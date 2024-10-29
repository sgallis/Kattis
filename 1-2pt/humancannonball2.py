#https://open.kattis.com/contests/xrjk7f/problems/humancannonball2

import sys
from math import radians, cos, sin
g = 9.81

def solution():
    n = int(input())
    for line in sys.stdin:
        v0, theta, x1, h1, h2 = map(float, line.split())
        theta = radians(theta)
        t1 = x1/(v0 * cos(theta))
        y1 = v0 * t1 * sin(theta) - 0.5*g*t1*t1
        if y1 - 1 >= h1 and h2 >= y1 + 1:
            sys.stdout.write("Safe\n")
        else:
            sys.stdout.write("Not Safe\n")

solution()