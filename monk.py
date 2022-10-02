#https://open.kattis.com/problems/monk
import sys
def solution():
    a, d = map(int, input().split())
    A = [[0, 0]]
    for i in range(a):
        h, t = map(int, sys.stdin.readline().split())
        A.append([A[i][0] + h, A[i][1] + t])
    D = [[A[-1][0], 0]]
    for i in range(d):
        h, t = map(int, sys.stdin.readline().split())
        D.append([D[i][0] - h, D[i][1] + t])
    D.reverse()
    ia = 0
    id = 0
    while A[ia][0] <= D[id][0]:
        if A[ia][1] <= D[id][1]:
            ia += 1
        else:
            id += 1
    ia -= 1
    timea = A[ia + 1][1] - A[ia][1]
    timed = D[id + 1][1] - D[id][1]
    hdiffa = A[ia + 1][0] - A[ia][0]
    hdiffd = D[id][0] - D[id + 1][0]
    print((D[id][0] - A[ia][0])/(hdiffa/timea - hdiffd/timed))
    

solution()
    
    
    
            

     