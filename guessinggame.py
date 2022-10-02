#https://open.kattis.com/problems/guessinggame

def solution():
    n = int(input())
    a = set(range(1, 11))
    while n != 0:
        command = input()   
        if command == "too high":
            a = a.intersection(set(range(1, n)))
        elif command == "too low":
            a = a.intersection(set(range(n + 1, 11)))
        else:
            if n in a:
                print("Stan may be honest")
            else:
                print("Stan is dishonest")
            a = set(range(1, 11))     
        n = int(input())

solution()