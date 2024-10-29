from string import ascii_uppercase


n, code, guess = input().split()
n = int(n)
r, s = 0, 0
# dictionary to compute s
code_dict = {i:0 for i in ascii_uppercase}
for x in code:
    code_dict[x] += 1
# compute r
for i in range(len(code)):
    if code[i] == guess[i]:
        r += 1
        code_dict[code[i]] -= 1
# compute s
for i in range(len(code)):
    if code[i] != guess[i] and code_dict[guess[i]]:
        s += 1
        code_dict[guess[i]] -= 1
print(r, s)


