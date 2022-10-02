# https://open.kattis.com/problems/putovanje

N, C = map(int, input().split())

fruits = list(map(int, input().split()))
real_eaten = 0

for i in range(len(fruits)):
    eaten = 0
    weight = 0
    for x in fruits[i:]:
        if weight + x <= C:
            eaten += 1
            weight += x
        else:
            pass
    if eaten >= real_eaten:
        real_eaten = eaten

print(real_eaten)