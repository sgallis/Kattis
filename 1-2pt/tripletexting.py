#https://open.kattis.com/contests/trhzg2/problems/tripletexting

def solution():
    word = input()
    word1 = word[:len(word)//3]
    word2 = word[len(word)//3:len(word)//3 * 2]
    word3 = word[len(word)//3 * 2:]
    if word1 == word2:
        print(word1)
    elif word2 == word3:
        print(word3)
    else:
        print(word1)

solution()
