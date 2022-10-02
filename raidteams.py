#https://open.kattis.com/problems/raidteams
import sys
from collections import deque

#a chaque fois que je trouve je pop
def findplayer(S1, players):
    player1 = S1.popleft()[1]
    while player1 in players:
        player1 = S1.popleft()[1]
    players.append(player1)
    return player1

def solution():
    n = int(input())
    S1 = list()
    S2 = list()
    S3 = list()
    players = list()
    for line in sys.stdin:
        L = line.split()
        name = L[0]
        S = list(map(int, L[1:]))
        S1.append((-S[0], name))
        S2.append((-S[1], name))
        S3.append((-S[2], name))
    S1.sort()
    S2.sort()
    S3.sort()
    S1 = deque(S1)
    S2 = deque(S2)
    S3 = deque(S3)
    player1 = None
    player2 = None
    player3 = None
    while True:
        if player1 == None and player2 == None and player3 == None and n - len(players) < 3:
            return
        elif player1 == None and player2 == None and player3 == None:
            player1 = findplayer(S1, players)
        elif player2 == None and player3 == None:
            player2 = findplayer(S2, players)
        elif player3 == None:
            player3 = findplayer(S3, players)
            L = [player1, player2, player3]
            L.sort()
            sys.stdout.write(f"{L[0]} {L[1]} {L[2]}\n")
            player1 = None
            player2 = None
            player3 = None
            
solution()         





