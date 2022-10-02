#https://open.kattis.com/problems/bazen

from math import sqrt, hypot

def calculator(result):
    if result >= 0:
        return f"{round(result * 100)//100}.{round(result * 100)%100//10}{round(result * 100)%10}"
    else:
        result = abs(result)
        return f"-{round(result * 100)//100}.{round(result * 100)%100//10}{round(result * 100)%10}"

def solution():
    x, y = map(float, input().split())
    trig_area = 250 ** 2 / 2
    if x==0 and y ==0:
        print("125.00 125.00")
    elif y == 0:
        if trig_area / x <= 250:
            print(f"0.00 {calculator(trig_area / x)}")
            return
        else:
            print(f"{calculator(250 - trig_area/(250-x))} {calculator(trig_area/(250-x))}")
            return
    elif x == 0:
        if trig_area / y <= 250:
            print(f"{calculator(trig_area / y)} 0.00")
            return
        else:
            print(f"{calculator(trig_area / (250 - y))} {calculator(250 - trig_area / (250 - y))}")
    else:
        if trig_area/x <= 250 and trig_area/x >=0:
            print(f"0.00 {calculator(250 - trig_area/x)}")
        else:
            print(f"{calculator(250 - trig_area/y)} 0.00")
solution()

