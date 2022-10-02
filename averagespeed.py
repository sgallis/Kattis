#https://open.kattis.com/problems/averagespeed

import sys

def calculator(result):
    if result >= 0:
        return(f"{round(result * 100)//100}.{round(result * 100)%100//10}{round(result * 100)%10}")
    else:
        result = abs(result)
        return(f"-{round(result * 100)//100}.{round(result * 100)%100//10}{round(result * 100)%10}")

def time(t1, t2):
    L1 = t1.split(":")
    L2 = t2.split(":")
    h1 = int(L1[0][0]) * 10 + int(L1[0][1])
    m1 = int(L1[1][0]) * 10 + int(L1[1][1])
    s1 = int(L1[2][0]) * 10 + int(L1[2][1])
    h2 = int(L2[0][0]) * 10 + int(L2[0][1])
    m2 = int(L2[1][0]) * 10 + int(L2[1][1])
    s2 = int(L2[2][0]) * 10 + int(L2[2][1])
    return ((h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1) / 3600


def solution():
    distance = 0
    all1 = sys.stdin.readline().split()
    time1 = all1[0]
    speed = int(all1[1])
    for line in sys.stdin:
        if len(line) > 11:
            all1 = line.split()
            time2 = all1[0]
            distance += time(time1, time2) * speed
            time1 = time2
            speed = int(all1[1])
        else:
            time2 = line
            distance += time(time1, time2) * speed
            time1 = time2
            print(time1[:len(time1) - 1], end = " ")
            print(f"{calculator(distance)} km")

solution()
