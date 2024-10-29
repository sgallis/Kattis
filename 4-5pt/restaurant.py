# https://open.kattis.com/problems/restaurant
import sys

def take(pile1, pile2, m):
    if pile1 >= m:
        sys.stdout.write(f"TAKE 1 {m}\n")
        pile1 -= m
    elif pile1 > 0:
        sys.stdout.write(f"TAKE 1 {pile1}\n")
        m -= pile1
        pile1 = 0

        sys.stdout.write(f"MOVE 2->1 {pile2}\n")
        pile1, pile2 = pile2, 0

        sys.stdout.write(f"TAKE 1 {m}\n")
        pile1 -= m
        
    elif pile1 == 0:
        sys.stdout.write(f"MOVE 2->1 {pile2}\n")
        pile1, pile2 = pile2, 0
        sys.stdout.write(f"TAKE 1 {m}\n")
        pile1 -= m
    return pile1, pile2

def drop(pile1, pile2, m):
    pile2 += m
    sys.stdout.write(f"DROP 2 {m}\n")
    return pile1, pile2

N = int(input())

while N!= 0:
    p1 = 0
    p2 = 0
    for _ in range(N):
        command, m = input().split()
        m = int(m)
        if command == "DROP":
            p1, p2 = drop(p1, p2, m)
        elif command == "TAKE":
            p1, p2 = take(p1, p2, m)

    sys.stdout.write("\n")
    N = int(input())
            




