#https://open.kattis.com/problems/8queens

import sys

def recup_diag(pos):
    possible = []
    #haut-droite
    indx = pos[0]
    indy = pos[1]
    while indx + 1 < 9 and indy - 1 > 0:
        indx += 1
        indy -= 1
        possible.append((indx, indy))
    #haut-gauche
    indx = pos[0]
    indy = pos[1]
    while indx - 1 > 0 and indy - 1 > 0:
        indx -= 1
        indy -= 1
        possible.append((indx, indy))
    #bas-droite
    indx = pos[0]
    indy = pos[1]
    while indx + 1 < 9 and indy + 1 < 9:
        indx += 1
        indy += 1
        possible.append((indx, indy))
    #bas-gauche
    indx = pos[0]
    indy = pos[1]
    while indx - 1 > 0 and indy + 1 < 9:
        indx -= 1
        indy += 1
        possible.append((indx, indy))
    
    return possible

def recup_lignes(pos):
    possible = []
    #haut
    indx = pos[0]
    indy = pos[1]
    while indy - 1 > 0:
        indy -= 1
        possible.append((indx, indy))
    #bas
    indx = pos[0]
    indy = pos[1]
    while indy + 1 < 9:
        indy += 1
        possible.append((indx, indy))
    #droite
    indx = pos[0]
    indy = pos[1]
    while indx + 1 < 9:
        indx += 1
        possible.append((indx, indy))
    #gauche
    indx = pos[0]
    indy = pos[1]
    while indx - 1 > 0:
        indx -= 1
        possible.append((indx, indy))
    
    return possible

def solution():
    i = 8
    queens = []
    for line in sys.stdin:
        j = 1
        for x in line:
            if x == "*":
                queens.append((j, i))
                break
            j += 1
        i -= 1
    L = []
    if len(queens) < 8:
        print("invalid")
        return
    for x in queens:
        L = L + recup_diag(x) + recup_lignes(x)
    for x in queens:
        if x in L:
            print("invalid")
            return
    print("valid")

solution()