#https://open.kattis.com/problems/ferryloading4

import sys

def solution():
    for _ in range(int(input())):
        l, m = map(int, sys.stdin.readline().split())
        l = l * 100
        left = list()
        right = list()
        left_count = 0
        right_count = 0
        
        for _ in range(m):
            line = sys.stdin.readline().split()
            if line[1] == "left":
                left.append(int(line[0]))
            else:
                right.append(int(line[0]))
        s = 0
        for i, x in enumerate(left):
            if s + x > l:
                s = x
                left_count += 1
            else:
                s += x  
            if i == len(left) - 1:
                left_count += 1
    
        s = 0
        for i, x in enumerate(right):
            if s + x > l:
                s = x
                right_count += 1
            else:
                s += x
            if i == len(right) - 1:
                right_count += 1

        if left_count == right_count:
            sys.stdout.write(f"{2 * left_count}\n")
        elif left_count > right_count:
            sys.stdout.write(f"{2 * left_count - 1}\n")
        else:
            sys.stdout.write(f"{2 * right_count}\n")

solution()
            

                    


