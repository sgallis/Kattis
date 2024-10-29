#https://open.kattis.com/contests/trhzg2/problems/krizaljka


def solution():
    word1, word2 = input().split()
    for i in word1:
        if i in word2:
            a = i
            break
    for i in range(len(word1)):
        if word1[i] == a:
            index = i
            break
    for i in range(len(word2)):
        if word2[i] == a:
            ind2 = i
            break
    for j in range(len(word2)):
        if j == ind2:
            print(word1)
        else:
            L = ["."] * index
            s = "".join(L)
            M = ["."] * (len(word1) - index - 1)
            m = "".join(M)
            print(f"{s}{word2[j]}{m}")

solution()
        