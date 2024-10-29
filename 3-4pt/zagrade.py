#https://open.kattis.com/contests/xrjk7f/problems/zagrade

from itertools import combinations

def find_brackets(expression):
    brackets = []
    used = []
    for i in range(len(expression)):
        if expression[i] == "(":
            right = 0
            for j in range(i + 1, len(expression)):
                if expression[j] == "(":
                    right += 1
                elif expression[j] == ")" and right > 0:
                    right -= 1
                elif expression[j] == ")" and j not in used:
                    used.append(j)
                    brackets.append((i, j))
                    break
    return brackets

def solution():
    operation = [x for x in input()]
    brackets = find_brackets(operation)
    comb = []
    expressions = []
    for i in range(1, len(brackets) + 1):
        comb.append(list(combinations(brackets, i)))
    for combis in comb:
        for combi in combis:
            expression = operation.copy()
            for x in combi:
                expression[x[0]] = " "
                expression[x[1]] = " "
            expression = "".join(expression).replace(" ", "")
            expressions.append(expression)
    expressions = list(set(expressions))
    expressions.sort()
    print("\n".join(expressions))

solution()
    
