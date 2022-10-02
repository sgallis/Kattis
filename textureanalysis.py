#https://open.kattis.com/problems/textureanalysis
import sys

def test_even(line, count):
    count = 0
    countsave = -1
    i = 1
    while i < len(line) and line[i] != "*":
        if line[i] == "*":
            if countsave == -1:
                countsave = count
            else:
                if countsave != count:
                    return False
                else:
                    count = 0
            i += 1
        else:
            count += 1
        i += 1
    return True
                
            
def solution():
    for line in sys.stdin:
        if line == "END":
            return
        else:
            if test_even(line, 0):
                sys.stdout.write("EVEN\n")
            else:
                sys.stdout.write("NOT EVEN\n")

solution()