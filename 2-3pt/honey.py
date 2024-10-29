#https://open.kattis.com/problems/honey

#a(n) is the number of paths from (0,0,0) to (n,n,n) 
# using the six permutations of (0,1,2) as steps, i.e., 
# the steps (0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), and (2,1,0).


def solution():
    L = [0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 1588356, 8676360, 47977776, 266378112, 1488801600]
    for _ in range(int(input())):
        print(L[int(input()) - 1])

solution()