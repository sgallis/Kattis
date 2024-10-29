# https://open.kattis.com/problems/antennaanalysis

n, c = map(int,input().split())

X = list(map(int,input().split()))
L = [0]
max1, max2 = c- X[0], X[0]+c
for j in range(1,n):
    
    if  c*(j+1)-X[j]  > max1:
        max1 = c*(j+1)-X[j]
    if X[j] + c*(j+1) > max2:
        max2 = X[j] + c*(j+1)
    L.append(max(X[j]-c*(j+1)+max1,-X[j]-c*(j+1)+max2))

    

print(" ".join(list(map(str,L))))