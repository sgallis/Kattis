##https://open.kattis.com/problems/industrialspy
from math import sqrt


def test_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def combinaisons(digits):
    if len(digits) == 1:
        return digits
    elif len(digits) == 2:
        return [digits[0] + digits[1] * 10, digits[1] + digits[0] * 10]
    else:
        L = []
        for i, x in enumerate(digits):
            l = len(digits) - 1
            a = [j + x * 10 ** l for j in combinaisons(digits[: i] + digits[i + 1 :])]
            L = L + a
        return L

def combinaisons1(digits):
    if len(digits) == 1:
        return digits
    else:
        L = []
        for i, x in enumerate(digits):
            a = [j for j in combinaisons(digits[: i] + digits[i + 1 :])]
            L = L + a
        return L

def combinaisons2(digits):
    L = []
    for i, x in enumerate(digits):
        a = [j for j in combinaisons1(digits[: i] + digits[i + 1 :])]
        L = L + a
    return L

def combinaisons3(digits):
    L = []
    for i, x in enumerate(digits):
        a = [j for j in combinaisons2(digits[: i] + digits[i + 1 :])]
        L = L + a
    return L

def combinaisons4(digits):
    L = []
    for i, x in enumerate(digits):
        a = [j for j in combinaisons3(digits[: i] + digits[i + 1 :])]
        L = L + a
    return L

def combinaisons5(digits):
    L = []
    for i, x in enumerate(digits):
        a = [j for j in combinaisons4(digits[: i] + digits[i + 1 :])]
        L = L + a
    return L

def combinaisons6(digits):
    L = []
    for i, x in enumerate(digits):
        a = [j for j in combinaisons5(digits[: i] + digits[i + 1 :])]
        L = L + a
    return L



def solution():
    n = int(input())
    for i in range(n):
        number = input()
        digits = [int(number[i]) for i in range(len(number))]
        l = len(digits) - 1
        N = 0
        for i, x in enumerate(digits):
            N += x * 10 ** (l - i)
        s = 0
        if N < 10:
            if test_prime(N):
                print(1)
            else:
                print(0)
        elif N < 100:
            for x in set(set(combinaisons(digits)).union(combinaisons1(digits))):
                if test_prime(x):
                    s += 1
            print(s)
        elif N < 1000:
            for x in set(set(combinaisons(digits)).union(combinaisons1(digits), combinaisons2(digits))):
                if test_prime(x):
                    s += 1
            print(s)
        elif N < 10000:
            for x in set(set(combinaisons(digits)).union(combinaisons1(digits), combinaisons2(digits), combinaisons3(digits))):
                if test_prime(x):
                    s += 1
            print(s)
        elif N < 100000:
            for x in set(set(combinaisons(digits)).union(combinaisons1(digits), combinaisons2(digits), combinaisons3(digits), combinaisons4(digits))):
                if test_prime(x):
                    s += 1
            print(s)
        elif N < 1000000:
            for x in set(set(combinaisons(digits)).union(combinaisons1(digits), combinaisons2(digits), combinaisons3(digits), combinaisons4(digits), combinaisons5(digits))):
                if test_prime(x):
                    s += 1
            print(s)
        elif N < 10000000:
            for x in set(set(combinaisons(digits)).union(combinaisons1(digits), combinaisons2(digits), combinaisons3(digits), combinaisons4(digits), combinaisons5(digits), combinaisons6(digits))):
                if test_prime(x):
                    s += 1
            print(s)


solution()
