#https://open.kattis.com/problems/busyschedule
import sys

def solution():
    a = int(input())
    while a != 0:
        timesam = []
        timespm = []
        for _ in range(a):
            time, marker = sys.stdin.readline().split()
            time = list(time.split(":"))
            time[0] = int(time[0]) % 12
            if marker == "a.m.":
                timesam.append(time)
            else:
                timespm.append(time)
        timesam.sort()
        timespm.sort()
        for j in timesam:
            sys.stdout.write(f"{(j[0] - 1) % 12 + 1}:{j[1]} a.m.\n")
        for j in timespm:
            sys.stdout.write(f"{(j[0] - 1) % 12 + 1}:{j[1]} p.m.\n")
        a = int(sys.stdin.readline())
        if a != 0:
            sys.stdout.write("\n")

solution()

