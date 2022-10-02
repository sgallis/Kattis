#https://open.kattis.com/problems/theplank

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solution(n - 3) + solution(n- 1) + solution(n - 2)


print(solution(int(input()))) 