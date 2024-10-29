#https://open.kattis.com/problems/saxophone

def solution():
    d = {"c":list(range(2,5)) + list(range(7,11)), "d":list(range(2,5)) + list(range(7,10))}
    d["e"] = list(range(2,5)) + list(range(7,9))
    d["f"] = list(range(2,5)) + [7]
    d["g"] = list(range(2,5))
    d['a'] = [2,3]
    d["b"] = [2]
    d["C"] = [3]
    d["D"] = list(range(1,5)) + list(range(7,10))
    d["E"] = [1,2,3,4,7,8]
    d["F"] = [1,2,3,4,7]
    d["G"] = [1,2,3,4]
    d["A"] = [1,2,3]
    d["B"] = [1,2]
    for _ in range(int(input())):
        pressed = []
        numbers = {i:0 for i in range(1, 11)}
        for i in input():
            topress = d[i]
            for j in topress:
                if j not in pressed:
                    numbers[j] += 1
            pressed = topress
        print(" ".join(map(str,numbers.values())))

solution()