from copy import deepcopy


N = int(input())
A = list(map(int, input().split()))
maxi, mini = A[0], min(A[2:])
mini_sort = deepcopy(A)
mini_sort.reverse()
for i in range(1,len(mini_sort)):
    if mini_sort[i] > mini_sort[i-1]:
        mini_sort[i] = mini_sort[i-1]
mini_sort.reverse()

n = 0
if A[0] == min(A):
    n += 1
if A[-1] == max(A):
    n += 1
for i in range(1, len(A) - 1):

    if A[i] > maxi and A[i] < mini:
        n += 1
    if i == len(A) - 2:
        break  
    if A[i] > maxi:
        maxi = A[i]
    if A[i+1] == mini:
        mini = mini_sort[i+2]
print(n)
