def differentiate(equation, point):
    res = []
    temp = equation[0]
    for i in range(1, len(equation)):
        if equation[i] in "+-":
            res.append(temp)
            res.append(equation[i])
            temp = ""
        else:
            temp += equation[i]
    res.append(temp)
    for i, j in enumerate(res):
        if j == "+" or j == "-":
            continue
        if "^" in j:
            flag = False
            if j[0] == "-":
                res[i] = j[1:]
                flag = True
            power = int(j[j.index("^")+1:])
            if res[i][0] == "x":
                res[i] = str(
                    point**(power-1)*power) if not flag else str(-(point**(power-1)*power))
            else:
                quotient = int(res[i][:res[i].index("x")])
                res[i] = str(
                    point**(power-1)*power*quotient) if not flag else str(-(point**(power-1)*power*quotient))
        elif "x" in res[i]:
            res[i] = "1" if len(j) == 1 else str((j[:j.index("x")]))
        else:
            res[i] = "0"
    return eval(" ".join(res))
