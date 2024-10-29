#https://open.kattis.com/problems/flexible

def solution():
    L = set()
    l, n = map(int, input().split())
    sections = [0] + list(map(int, input().split())) + [l]
    #print(sections)
    for i in sections:
        for j in sections:
            if i-j != 0:
                L.add(abs(i-j))
    print(" ".join(map(str, sorted(list(L)))))

solution()
    
