#https://open.kattis.com/problems/calculator
import sys
def solution():
    for operation in sys.stdin:
        result = eval(operation)
        if result >= 0:
            sys.stdout.write(f"{round(result * 100)//100}.{round(result * 100)%100//10}{round(result * 100)%10}\n")
        else:
            result = abs(result)
            sys.stdout.write(f"-{round(result * 100)//100}.{round(result * 100)%100//10}{round(result * 100)%10}\n")

solution()

