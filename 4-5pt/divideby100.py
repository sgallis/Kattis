from copy import deepcopy


N = list(map(int, input()))
M = list(input())

dot = len(N)-len(M) +1

if dot >= 1: # N>M
    Nbis = deepcopy(N)
    Nbis = N[dot:]
    while Nbis and not Nbis[-1]:
        Nbis.pop()
    if Nbis:
        print("".join(map(str,N[:dot]))+"."+"".join(map(str,Nbis)))
    else:
        print("".join(map(str,N[:dot])))
else:
    while N and not N[-1]:
        N.pop()
    zeros = "".join(map(str, [0 for _ in range(abs(dot))]))
    print("0."+ zeros +"".join(map(str, N)))