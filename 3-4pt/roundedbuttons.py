#https://open.kattis.com/problems/roundedbuttons

import sys
from math import sqrt

def inside_rectangle(xclick, yclick, x, y, w, h):
    return (xclick >= x and xclick <= x + w and yclick >= y and yclick <= y + h)

def circles(x, y, w, h, r):
    return [(x+r, y+r), (x+w-r, y+r), (x+r, y+h-r), (x+w-r, y+h-r)]

def inside_circle(x, y, xcenter, ycenter, r):
    return sqrt((x-xcenter)*(x-xcenter) + (y-ycenter)*(y-ycenter)) <= r

def test_circles(xclick, yclick, x, y, w, h, r):
    for coord in circles(x,y,w,h,r):
        if inside_circle(xclick, yclick, coord[0],coord[1],r):
            return True
    return False

def solution():
    n = int(input())
    for line in sys.stdin:
        L = list(map(float, line.rstrip("\n").split()))
        x, y, w, h, r = L[:5]
        for i in range(6, len(L), 2):
            xclick, yclick = L[i], L[i+1]
            if not inside_rectangle(xclick,yclick,x,y,w,h):
                sys.stdout.write("outside\n")
            elif xclick >= x+r and xclick <= x+w-r:
                sys.stdout.write("inside\n")
            elif yclick >= y+r and yclick <= y+h-r:
                sys.stdout.write("inside\n")     
            elif test_circles(xclick, yclick, x, y, w, h, r):
                sys.stdout.write("inside\n")
            else:
                sys.stdout.write("outside\n")
        sys.stdout.write("\n")

solution()