#https://open.kattis.com/contests/trhzg2/problems/karte

def solution():
    a = True
    if a:
        P = []
        K = []
        H = []
        T = []
        a = input()
        for i in range(0, len(a), 3):
            if a[i] == "P":
                s = a[i+1] + a[i + 2]
                if s in P:
                    print("GRESKA")
                    return
                else:
                    P.append(s)
            elif a[i] == "K":
                s = a[i+1] + a[i + 2]
                if s in K:
                    print("GRESKA")
                    return
                else:
                    K.append(s)
            elif a[i] == "H":
                s = a[i+1] + a[i + 2]
                if s in H:
                    print("GRESKA")
                    return
                else:
                    H.append(s)
            elif a[i] == "T":
                s = a[i+1] + a[i + 2]
                if s in T:
                    print("GRESKA")
                    return
                else:
                    T.append(s)
        print(f"{13-len(P)} {13-len(K)} {13-len(H)} {13-len(T)}")
solution()


