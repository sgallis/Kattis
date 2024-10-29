#https://open.kattis.com/problems/closestsums
import sys

def solution():
    booln = False
    boolm = False
    case = 0
    numbers = []
    possibilities = []
    for line in sys.stdin:
        k = int(line)
        if not booln:
            booln = True
            indn = 0
            case += 1
            n = k
        else:
            if indn == 0:
                sys.stdout.write(f"Case {case}:\n")
            if indn < n:
                numbers.append(k)
                indn += 1
                if len(numbers) >= 2:
                    for i in numbers[0:-1]:
                        possibilities.append(i + k)
            else:
                if not boolm:
                    boolm = True
                    indm = 0
                    m = k
                else:
                    if indm < m:
                        distances = []
                        for y in possibilities:
                                distances.append((abs(y-k), y))

                        sys.stdout.write(f"Closest sum to {k} is {min(distances)[1]}.\n")
                        
                        indm += 1
                    else:
                        
                        boolm = False
                        booln = True
                        n = k
                        case += 1
                        indn = 0
                        numbers = []
                        instructions = []
solution()

            


            

