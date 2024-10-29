#https://open.kattis.com/problems/anotherbrick

def solution():
    h, w , n = tuple(map(int, input().split()))
    bricks = list(map(int, input().split()))
    etage = 0
    wi = w
    for i, l in enumerate(bricks):
        wi -= l
        if wi == 0:
            etage += 1
            wi = w
            if etage == h:
                print("YES")
                break
        elif wi < 0:
            print("NO")
            break
solution()