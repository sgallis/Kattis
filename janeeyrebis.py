#https://open.kattis.com/problems/janeeyre

import sys
from bisect import insort
from collections import deque


def solution():
    n, m, jane_pages = map(int, sys.stdin.readline().split())
    title = "Jane Eyre"
    stack = [("Jane Eyre", jane_pages)]
    time = 0
    unread = list()
    for _ in range(n):#pile
        line = sys.stdin.readline().lstrip("\"").rstrip("\n").split("\"")
        line[1] = int(line[1].strip())
        line = tuple(line)
        if line[0] < title:
            stack.append(line)
    stack.sort()
    stack = deque(stack)
    for _ in range(m): #friends give
        line = sys.stdin.readline().lstrip("\"").rstrip("\n").split("\"")
        line[0] = int(line[0].strip())
        line[2] = int(line[2].strip())
        if line[1] < title:
            unread.append(line)
    unread.sort()
    unread = deque(unread)
    while len(stack) > 1:
        if unread == deque():
            time += stack.popleft()[1]
        elif unread[0][0] <= time + stack[0][1]:
            insort(stack, tuple(unread.popleft()[1:]))
        else:
            time += stack.popleft()[1]
    print(time + jane_pages)

solution()
