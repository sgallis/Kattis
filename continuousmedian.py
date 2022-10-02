# https://open.kattis.com/problems/continuousmedian


T = int(input())

for _ in range(T):
    s = 0
    A = list(map(int, input().split()))
    for i in range(len(A)):
        if not i:
            s +=A[i]
        else:
            if not i - 1: # longueur de 2
                gauche = A[0]
                droite = A[1]
                s += (gauche+droite)//2
            elif not i - 2: # longueur de 3
                a = A[i]
                if a < gauche:
                    milieu, gauche = gauche, a
                elif a > droite:
                    milieu, droite = droite, a
                else:
                    milieu = a
                s += milieu
            elif not i % 2: # longueur impaire
                a = A[i]
                if a < gauche:
                    gauche, milieu = max(a, anciengauche), gauche

                elif a > droite:

                    droite, milieu = min(a, anciendroite), droite
                else:
                    milieu = a
                s += milieu
            else: # longueur paire  # gauche milieu droite
                a = A[i]
                if a <= gauche:
                    s += (milieu+gauche)//2
                    droite = milieu
                elif a >= droite:
                    s += (milieu+droite)//2
                    gauche = milieu
                else:
                    s += (milieu+a)//2
                    
                    if a <= milieu:
                        gauche, droite = a, milieu
                    else:
                        gauche, droite = milieu, a
    print(s)


