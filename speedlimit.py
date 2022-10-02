#https://open.kattis.com/problems/speedlimit
import sys

def solution():
    n = int(input())
    while n != -1:
        time = 0
        distance = 0
        for _ in range(n):
            speed, total = map(int,sys.stdin.readline().split())
            distance += speed * (total - time)
            time = total
        print(f"{distance} miles")
        n = int(sys.stdin.readline())

solution()

