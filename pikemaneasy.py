#https://open.kattis.com/problems/pikemaneasy


def solution():
    N, T = map(int, input().split())
    A, B, C, t0 = map(int, input().split())
    times = [t0]
    for j in range(1, N):
        times.append((A * times[j - 1] + B) % C + 1)
    times.sort()
    penalty = 0
    i = 0
    l = len(times)
    time = 0
    for i, t in enumerate(times):
        if time + t <= T:
            time += t
            penalty = (penalty + time) % 1000000007
        else:
            print(f"{i} {penalty}")
            return
    print(f"{l} {penalty}")
    



solution()

    
    
    

    #the time in minutes from contest start was added to a penalty counter  
    #faire une fonction récursive