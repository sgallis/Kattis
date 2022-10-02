def convertint(word):
    i = 0
    while word[i] =="0":
        i += 1
    if i == len(word) - 1:
        return 0
    return int(word[i:])
    
T = int(input())
reference = {"lower":"0", "middle":"1", "upper":"2"}
for _ in range(T):
    n = int(input())
    people = list()
    for _ in range(n):
        name, echelle = input().split(": ")
        echelle = echelle.rstrip(" class")
        echelle = [reference[i] for i in echelle.split("-")]
        echelle.reverse()
        while len(echelle) < 10:
            echelle.append("1")
        echelle = "".join(echelle)
        echelle = (-convertint(echelle),name)
        people.append(echelle)
    people.sort()
    for i in people:
        print(i[1])
    print("".join(["="for _ in range(30)]))
        

