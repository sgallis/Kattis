#https://open.kattis.com/problems/soundex

def solution():
    while True:
        s = ""
        a = ""
        try:
            word = input()
            if word == "":
                break
            for i in word:
                if i in ["B", "F", "P", "V"]:
                    if len(s) == 0:
                        s = s + str(1)
                        a = "1"
                    elif a != "1" or a == "":
                        s = s + str(1)
                        a = "1"
                    
                elif i in ["C", "G", "J", "K", "Q", "S", "X", "Z"]:
                    if len(s) == 0:
                        s = s + str(2) 
                        a = "2"
                    elif a != "2" or a == "":
                        s = s + str(2) 
                        a = "2"   
                elif i == "D" or i == "T":
                    if len(s) == 0:
                        s = s + str(3)
                        a = "3"
                    elif a != "3" or a == "":
                        s = s + str(3)
                        a = "3"
                elif i == "L":
                    if len(s) == 0:
                        s = s + str(4)
                        a = "4"
                    elif a != "4" or a == "":
                        s = s + str(4)
                        a = "4"
                elif i == "M" or i == "N":
                    if len(s) == 0:
                        s = s + str(5)
                        a = "5"
                    elif a != "5" or a == "":
                        s = s + str(5)
                        a = "5"
                elif i == "R":
                    if len(s) == 0:
                        s = s + str(6)
                        a = "6"
                    elif a != "6" or a == "":
                        s = s + str(6)
                        a = "6"
                else:
                    a = ""
            print(s)
        except:
            break

solution()