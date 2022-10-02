#https://open.kattis.com/problems/rotatecut
import sys

def solution():
    _ = input()
    for line in sys.stdin:
        n, sentence = line.split()
        n = int(n)
        for i in range(n):
            if len(sentence) < 4:
                break
            elif i % 2 == 0:
                sentence = sentence[len(sentence) // 4:]
            else:
                sentence = sentence[:len(sentence) - len(sentence) // 4 ]
        print(sentence)

solution()

