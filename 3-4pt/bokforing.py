# https://open.kattis.com/problems/bokforing

import sys
N, Q = map(int, input().split())
value = 0
modified = dict()
for _ in range(Q):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "RESTART":
        modified = dict()
        value = int(command[-1])
    elif command[0] == "PRINT":
        i = int(command[1])
        if i not in modified:
            sys.stdout.write(f"{value}\n")
        else:
            sys.stdout.write(f"{modified[i]}\n")
    else:
        i, x = map(int, command[1:])
        modified[i] =x

