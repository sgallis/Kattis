import sys
definitions = dict()
redefinitions = dict()
for line in sys.stdin:
    # print(definitions, redefinitions)
    command = line.rstrip().split()
    if command[0] == "def":
        if command[1] in redefinitions:
            key = redefinitions.pop(command[1])
            definitions.pop(key)
        definitions[int(command[-1])] = command[1]
        redefinitions[command[1]] = int(command[-1])
    elif command[0] == "clear":
        definitions = dict()
        redefinitions = dict()
    else:
        variables = command[1:-1:2]
        signs = command[2:-1:2]
        if False in [False for v in variables if v not in redefinitions]:
            sys.stdout.write(" ".join(command[1:]) + " unknown\n")
        else:
            result = redefinitions[variables[0]]
            i = 1
            for s in signs:
                if s == "+":
                    result += redefinitions[variables[i]]
                    i += 1
                else:
                    result -= redefinitions[variables[i]]
                    i += 1
            # print(result)
            if result not in definitions:
                sys.stdout.write(" ".join(command[1:]) + " unknown\n")
            else:
                sys.stdout.write(" ".join(command[1:]) + f" {definitions[result]}\n")
        
