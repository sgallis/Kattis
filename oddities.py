#https://open.kattis.com/contests/bxmyat/problems/oddities

def solution():
    for _ in range(int(input())):
        i = int(input())
        if abs(i)%2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

solution()