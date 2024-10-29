#https://open.kattis.com/problems/temperatureconfusion

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def solution():
    a, b = tuple(map(int, input().split("/")))
    #(F - 32) *5/9
    a = (a - 32 * b) * 5
    b = b * 9
    c = pgcd(a, b)
    print(f"{a//c}/{b//c}")

solution()
