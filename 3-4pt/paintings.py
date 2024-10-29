#https://open.kattis.com/problems/paintings

import sys
#import heapq


def solution():
    T = int(input())
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip("\n"))
        colors = sys.stdin.readline().rstrip("\n").split()
        n = len(colors)
        dict_numbers = [colors[i] for i in range(n)]
        dict_colors = {colors[i] : i for i in range(n)}
        hideous = [[] for i in range(n)]
        M = int(sys.stdin.readline().rstrip("\n"))
        for _ in range(M):
            color1, color2 = sys.stdin.readline().rstrip("\n").split()
            color1, color2 = dict_colors[color1], dict_colors[color2]
            hideous[color1].append(color2)
            hideous[color2].append(color1)
        numbers = 0
        # parcours en profondeur
        tas = [[i] for i in range(n)]
        compte = False
        """for i in range(n):
            heapq.heappush(tas, [i])"""
        while tas:
            #a = heapq.heappop(tas)
            a = tas.pop()
            # traitement
            if not compte and len(a) == n:
                favorite = a
                numbers += 1
                compte = True
            elif len(a) == n:
                numbers += 1
                if favorite >= a:
                    favorite = a
            else:
                for i in range(n):
                    if i not in hideous[a[-1]] and i not in a:
                        c = a.copy()
                        c.append(i)
                        #heapq.heappush(tas, c)
                        tas.append(c)

        sys.stdout.write(f"{numbers}\n")
        sys.stdout.write(" ".join([dict_numbers[i] for i in favorite])+"\n")

solution()


            

