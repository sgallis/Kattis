#https://open.kattis.com/problems/bachetsgame
import sys

def solution():
    for line in sys.stdin:
        L = list(map(int, line.split()))
        n, stones, m = L[0], L[1:-1], L[-1]


if __name__ == "__main__":
    solution()