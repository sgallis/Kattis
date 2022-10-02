#https://open.kattis.com/problems/aboveaverage

def solution():
    c = int(input())
    for i in range(c):
        a = input().split(" ")
        n = int(a[0])
        m = 0
        for j in range(1, len(a)):
            m += int(a[j])
        m = m / n
        nb = 0
        for j in range(1, len(a)):
            if int(a[j]) > m:
                nb += 1
        pr = round(100000 * nb/n)
        if pr % 1000 == 0:
            pr = pr // 1000
            print(f"{pr}.000%")
        elif pr % 100 == 0:
            pr = pr // 100
            print(f"{pr}00%")
        elif pr % 10 == 0:
            pr = pr // 10
            print(f"{pr}0%")
        else:
            pr = pr / 1000
            print(f"{pr}%")

solution()

