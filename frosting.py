# https://open.kattis.com/problems/frosting

import sys

n = int(input())

yellow, pink, white = [0 for _ in range(3)]

A = list(map(int, input().split()))
B = list(map(int, input().split()))

b1 = sum([B[i] for i in range(0, len(B),3)])
b2 = sum([B[i] for i in range(1, len(B),3)])
b3 = sum([B[i] for i in range(2, len(B),3)])
for i in range(0,len(A)):
    if i%3==0:
        white += A[i]*b1 
        yellow += A[i] * b2
        pink += A[i]*b3
    elif i%3==1:
        yellow += A[i]*b1
        pink += A[i]*b2
        white += A[i]*b3
    else:
        pink += A[i]*b1
        white += A[i]*b2
        yellow += A[i]*b3



print(yellow, pink, white)

