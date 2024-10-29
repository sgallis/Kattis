# https://open.kattis.com/contests/pzmq28/problems/knotknowledge

n = int(input())
to_learn = set(map(int,input().split()))
learned = set(map(int, input().split()))

print(list(to_learn.difference(learned))[0])