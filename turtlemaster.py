# https://open.kattis.com/problems/turtlemaster

matrice = []

for _ in range(8):
    matrice.append(list(input()))

matrice.reverse()

impression = False
position = (0, 0)
rotation = (1, 0)
diamond = False

commands = list(input())

for commande in commands:
    x, y = position[0] + rotation[0], position[1] + rotation[1] 
    if commande == "F": 
        diamond = False
        if x in list(range(0, 8)) and y in list(range(0, 8)) and matrice[y][x] != "C" and matrice[y][x] != "I":
            position = (x, y)
            if matrice[y][x] == "D":
                diamond = True
        else:
            print("Bug!")
            impression = True
            break
    elif commande == "R":
        if rotation == (1, 0):
            rotation = (0, -1)
        elif rotation == (0, -1):
            rotation = (-1, 0)
        elif rotation == (-1, 0):
            rotation = (0, 1)
        else:
            rotation = (1, 0)
    elif commande == "L":
        if rotation == (1, 0):
            rotation = (0,1)
        elif rotation == (0, 1):
            rotation = (-1, 0)
        elif rotation == (-1, 0):
            rotation = (0, -1)
        else:
            rotation = (1, 0)
    else:
        if x in list(range(0, 8)) and y in list(range(0, 8)) and matrice[y][x] == "I":
            matrice[y][x] = "."
        else:
            print("Bug!")
            impression = True
            break
if diamond and not impression:
    print("Diamond!")
elif not impression:
    print("Bug!")

