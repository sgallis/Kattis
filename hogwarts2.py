#https://open.kattis.com/problems/hogwarts2

import sys

def prochain_room(room_number, exit_1, map1):
    return map1[room_number][exit_1 - 1]
    
def solution():
    n = int(input())
    map1 = [False]
    for _ in range(n):
        map1.append(tuple(map(int, sys.stdin.readline().rstrip("\n").split())))
    # parcours de tous les chemins possibles
    paths = set()                                      
    tas = [[1, i, 1] for i in range(1,5)] # number of the room, exit to take, exits taken
    while tas:
        print(tas)
        room = tas.pop()
        room_number, exit = room[0], room[1]
        prochain = prochain_room(room_number, exit, map1)
        if prochain == 0:
            pass
        elif prochain == n:
            room.append(exit)
            paths.add(tuple(room[2:]))
        elif len(room[2:]) == n:
            pass
        elif prochain not in room[2:]:
            for i in range(1, 5):
                tas.append([prochain, i, *room[2:], exit])
    if not paths:
        print("Impossible")
    # test pour la deuxieme carte
    map2 = [False]
    for _ in range(n):
        map2.append(tuple(map(int, sys.stdin.readline().rstrip("\n").split())))
    for path in paths:
        a = "k"
        for x in path:
            if a == "k":
                a = 1
            else:
                a = prochain_room(a, x, map2)
            if a == 0:
                break
            elif a == 4:
                print("Yes")
                return
    print("No")

solution()

    

