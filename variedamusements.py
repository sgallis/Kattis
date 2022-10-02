#https://open.kattis.com/problems/variedamusements

def note(TD, P, TP):
    return (TD*0.09 + P*0.8*0.9 + TP*0.1+ 14.82*0.09)

s= 0
tot = 0
for TD in range(11,17):
    for P in range(4,11):
        for TP in range(9, 15):
            if note(TD, P, TP) >= 10:
                validé = True
                s+= 1
            else:
                validé = False
            tot += 1
            print(f"TD:{TD} P: {P} TP:{TP}  {validé} {note(TD,P, TP)}")

print(s/tot)




