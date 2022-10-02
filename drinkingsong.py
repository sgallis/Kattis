#https://open.kattis.com/contests/xrjk7f/problems/drinkingsong
import sys

def solution():
    n = int(input())
    beverage = input()
    while n > 0:
        if n > 2:
            sys.stdout.write(f"{n} bottles of {beverage} on the wall, {n} bottles of {beverage}.\nTake one down, pass it around, {n - 1} bottles of {beverage} on the wall.\n")
        elif n == 2:
            sys.stdout.write(f"{n} bottles of {beverage} on the wall, {n} bottles of {beverage}.\nTake one down, pass it around, {n - 1} bottle of {beverage} on the wall.\n")
        else:
            sys.stdout.write(f"{n} bottle of {beverage} on the wall, {n} bottle of {beverage}.\nTake it down, pass it around, no more bottles of {beverage}.\n")
        if n > 1:
            sys.stdout.write(f"\n")
        n -= 1
solution()