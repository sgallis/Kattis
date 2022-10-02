# https://open.kattis.com/problems/glossaryarrangement

import sys

n, w = map(int, input().split())

words = [sys.stdin.readline().rstrip() for _ in range(n)]
words_vrai = [[i] for i in words]

r = n
c = 0 # nb colonnes
for i in words:
    if len(i) >=c:
        c = len(i)

while c <= w:
    words_tempo =
