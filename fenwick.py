# https://open.kattis.com/problems/fenwick

import sys


class FenwickTree():
    def __init__(self, n):
        self.L = [0] * (n + 1)
        self.size = n + 1

    def update(self, i, diff):
        i += 1
        while i < self.size:
            self.L[i] += diff
            i += i & -i

    def sum(self, i):
        result = 0
        while i > 0:
            result += self.L[i]
            i = i & (i - 1)
        return result


def solution():
    N, Q = map(int, input().split())
    tree = FenwickTree(N)
    for line in sys.stdin:
        command = line.split()
        if command[0] == "+":
            tree.update(int(command[1]), int(command[2]))
        else:
            if command[1] == "0":
                sys.stdout.write("0\n")
            else:
                sys.stdout.write(f"{tree.sum(int(command[1]))}\n")


solution()
