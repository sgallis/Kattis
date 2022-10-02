#https://open.kattis.com/problems/anagramcounting
from math import factorial

def anagram(L):
    if max(L) == 1:
        return factorial(len(L))
    elif len(L) == 1:
        return 1
    else:
        s = sum(L)
        l = L[-1]
        return anagram(L[: -1]) * factorial(s) // factorial(l) // factorial(s - l)

def solution():
    while True:
        try:
            word = input()
            d = {}
            for j in range(len(word)):
                d.setdefault(ord(word[j]), 0)
                d[ord(word[j])] += 1
            val = list(d.values())
            print(anagram(val))
        except:
            break

solution()
