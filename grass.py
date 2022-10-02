# https://open.kattis.com/problems/grass

import sys

for line in sys.stdin:
    line = map(int, line.rstrip("\n").split())
    if len(line) == 2:
        n, l, w = line
        sprinklers = []
    else:
        sprinklers.append(line) # line = [x, r]
        
