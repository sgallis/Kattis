# https://open.kattis.com/problems/uxuhulvoting

import sys
from collections import deque


def solution():
    possibilities = ["NNN", "NNY", "NYN", "NYY", "YNN", "YNY", "YYN", "YYY"]
    n = int(input())
    for _ in range(n):
        m = int(sys.stdin.readline())
        L = deque()
        for _ in range(m):
            L.append(list(map(int, sys.stdin.readline().split())))
