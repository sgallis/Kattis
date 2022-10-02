# https://open.kattis.com/problems/cakeymccakeface

N = int(input())
M = int(input())

entries = list(map(int,input().split()))
exits = list(map(int, input().split()))

times = dict()

for n in range(N):
    for m in range(M):
        if exits[m] >= entries[n]:
            time = exits[m] - entries[n]
            times.setdefault(time, 0)
            times[time] += 1
occ = 0
time = 0

for x in times:

    if times[x] > occ:
        time = x
        occ = times[x]
    elif times[x] == occ:
        if x < time:
            time = x
print(time)