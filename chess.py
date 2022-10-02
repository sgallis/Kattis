#https://open.kattis.com/problems/chess
import sys

def test_white(pos):
    even = ["A", "C", "E", "G"]
    odd = ["B", "D", "F", "H"]
    if pos[0] in even:
        return int(pos[1]) % 2 == 0
    else:
        return int(pos[1]) % 2 == 1

def recup_diag(pos):
    L = []   
    letters = [chr(i) for i in range(65, 73)]
     
    #haut-droite
    ind = int(pos[1])
    letter = pos[0]
    while ind < 9 and letter in letters and ind > 0:
        L.append(f"{letter}{ind}")
        ind += 1
        letter = chr(ord(letter) + 1)
    
    #bas-droite
    ind = int(pos[1])
    letter = pos[0]
    while ind < 9 and letter in letters and ind > 0:
        L.append(f"{letter}{ind}")
        ind -= 1
        letter = chr(ord(letter) + 1)
     #haut-gauche
    ind = int(pos[1])
    letter = pos[0]
    while ind < 9 and letter in letters and ind > 0:
        L.append(f"{letter}{ind}")
        ind += 1
        letter = chr(ord(letter) - 1)
    #bas-gauche
    ind = int(pos[1])
    letter = pos[0]
    while ind < 9 and letter in letters and ind > 0:
        L.append(f"{letter}{ind}")
        ind -= 1
        letter = chr(ord(letter) - 1)
    return L

def test_diag(init_pos, end_pos):
    return end_pos in recup_diag(init_pos)

def solution():
    for _ in range(int(input())):
        moves = sys.stdin.readline().split()
        init_pos = moves[0] + moves[1]
        end_pos = moves[2] + moves[3]
        if test_white(init_pos) != test_white(end_pos):
            sys.stdout.write("Impossible\n")
        else:
            if init_pos == end_pos:
                sys.stdout.write(f"0 {init_pos[0]} {init_pos[1]}\n")
            elif test_diag(init_pos, end_pos):
                sys.stdout.write(f"1 {init_pos[0]} {init_pos[1]} {end_pos[0]} {end_pos[1]}\n")
            else:
                init = recup_diag(init_pos)
                end = recup_diag(end_pos)
                for i in init:
                    if i in end:
                        sys.stdout.write(f"2 {init_pos[0]} {init_pos[1]} {i[0]} {i[1]} {end_pos[0]} {end_pos[1]}\n")
                        break

solution()