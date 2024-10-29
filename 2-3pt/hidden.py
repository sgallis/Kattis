# https://open.kattis.com/problems/hidden

pwd, sentence = map(list, input().split())

pwd.reverse()
raté = False
for i in sentence:
    if i not in pwd:
        pass
    else:
        if i == pwd[-1]:
            pwd.pop()
            if not pwd:
                print("PASS")
                break
        else:
            print("FAIL")
            raté = True
            break
if pwd and not raté:
    print("FAIL")
        
