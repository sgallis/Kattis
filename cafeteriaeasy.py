#https://open.kattis.com/contests/xrjk7f/problems/cafeteriaeasy

def solution():
    line1 = input().split()
    line2 = input().split()
    salamender = line1[:2] + line2[:2]
    yeti = line1[2:4] + line2[2:4]
    golem = line1[4:6] + line2[4:6]
    imp = line1[6: 8] + line2[6:8]
    kraken = line1[8:] + line2[8:]
    
    burgers = line1[::2]
    slop = line1[1::2]
    sushi = line2[::2]
    drumstick = line2[1::2]
    
    #burgers, slop, sushi, drumstick

solution()