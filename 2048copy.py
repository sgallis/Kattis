#https://open.kattis.com/problems/2048
def transpose(L):
    return [[L[i][j] for i in range(len(L))] for j in range(len(L))]

def solution():
    L = [list(map(int, input().split())) for i in range(4)]
    move = int(input())
    if move == 0:
        for j in range(4):
            M = []
            for k in range(4):
                if L[j][k] != 0:
                    M.append(L[j][k])
            i = 0
            while i < len(M) - 1:
                if M[i] == M[i + 1]:
                    M[i] = 2 * M[i + 1]
                    M[i + 1] = 0
                    i += 2
                else:
                    i += 1
            N = []
            for x in range(len(M)):
                if M[x] != 0:
                    N.append(M[x])
            while len(N) < 4:
                N.append(0)
            for k in range(4):
                L[j][k] = N[k]

    elif move == 2:
        for j in range(4):
            M = []
            for k in range(4):
                if L[j][k] != 0:
                    M.append(L[j][k])
            i = len(M) - 1
            while i > 0:
                if M[i] == M[i - 1]:
                    M[i] = 2 * M[i - 1]
                    M[i - 1] = 0
                    i -= 2
                else:
                    i -= 1
            N = []
            for x in range(len(M)):
                if M[x] != 0:
                    N.append(M[x])       
            while len(N) < 4:
                N = [0] + N
            for k in range(4):
                L[j][k] = N[k]
    elif move == 1:
        B = transpose(L)
        for j in range(4):
            M = []
            for k in range(4):
                if B[j][k] != 0:
                    M.append(B[j][k])
            i = 0
            while i < len(M) - 1:
                if M[i] == M[i + 1]:
                    M[i] = 2 * M[i + 1]
                    M[i + 1] = 0
                    i += 2
                else:
                    i += 1
            N = []
            for x in range(len(M)):
                if M[x] != 0:
                    N.append(M[x])     
            while len(N) < 4:
                N.append(0)
            for k in range(4):
                B[j][k] = N[k]
        L = transpose(B)   
    else:
        B = transpose(L)
        for j in range(4):
            M = []
            for k in range(4):
                if B[j][k] != 0:
                    M.append(B[j][k])
            i = len(M) - 1                                              
            while i > 0:
                if M[i] == M[i - 1]:
                    M[i] = 2 * M[i - 1]
                    M[i - 1] = 0
                    i -= 2
                else:
                    i -= 1
            N = []
            for x in range(len(M)):
                if M[x] != 0:
                    N.append(M[x])    
            while len(N) < 4:
                N = [0] + N
            for k in range(4):
                B[j][k] = N[k]
        L = transpose(B)
    for i in range(4):
        a = ""
        for j in range(4):
            if j == 3:
                a = a + f"{int(L[i][j])}"
            else:
                a = a + f"{int(L[i][j])} "
        print(a)

solution()
