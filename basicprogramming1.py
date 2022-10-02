#https://open.kattis.com/problems/basicprogramming1
import string

def mod(n):
    return n%26
def dkd(n):
    return chr(mod(n)+97)
def solution(t, A, N):
    if t == 1:
        print(7)
    elif t == 2:
        if A[0] > A[1]:
            print("Bigger")
        elif A[0] == A[1]:
            print("Equal")
        else:
            print("Smaller")
    elif t == 3:
        L = [A[0], A[1], A[2]]
        L.sort()
        print(L[1])
    elif t == 4:
        print(sum(A))
    elif t == 5:
        print(sum(i for i in A if i%2==0 )) 
    elif t == 6:
        print("".join(map(dkd, A)))
    else:
        i = 0
        L = [True] + (N - 1) * [False]
        while True:
            i = A[i]
            if i > N - 1:
                print("Out")
                break
            elif i == N-1:
                print("Done")
                break
            if L[i] == True:
                print("Cyclic")
                break
            L[i] = True

            


if __name__ == '__main__':
    N, t = map(int, input().split())
    A = list(map(int, input().split()))
    solution(t,A,N)

