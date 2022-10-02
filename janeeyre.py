#https://open.kattis.com/problems/janeeyre

import sys

def solution():
    n, m, jane_pages = map(int, sys.stdin.readline().split())
    title = "Jane Eyre"
    unread = list()
    time = 0
    for _ in range(n):#pile
        line = sys.stdin.readline().lstrip("\"").rstrip("\n").split("\"")
        line[1] = int(line[1].strip())
        line = tuple(line)
        if line[0] < title:
            time += line[1]
    for _ in range(m): #friends give
        line = sys.stdin.readline().lstrip("\"").rstrip("\n").split("\"")
        line[0] = int(line[0].strip())
        line[2] = int(line[2].strip())
        if line[1] < title:
            unread.append(line)
    unread.sort()
    i = 0
    while i < len(unread) and unread[i][0] <= time:
        time += unread[i][2]
        i += 1
    print(time + jane_pages)

solution()