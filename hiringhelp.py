# https://open.kattis.com/contests/pzmq28/problems/hiringhelp
import sys


n = int(input())
coders = list()
consultants = [True for _ in range(n)]
lines, bugs = [][]
for _ in range(n):
    line, bug = map(int, input().split())
    coders.append([line, bug])
    lines += line   
    bugs += bug

e = int(input())

for _ in range(e):
    command = input().split()
    if command[0]== "q": # coder quits
       lines -= coders[int(command[1])-1][0]
       bugs -= coders[int(command[1])-1][1]
    else: # hire a consultant
        t, l, f = map(int, command[1:])
        if l > lines and f > bugs:
            sys.stdout.write("yes\n")
        else:
            sys.stdout.write("no\n")