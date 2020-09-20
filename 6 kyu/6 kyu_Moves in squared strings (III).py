def rot_90_clock(s):
    temp = s.split("\n")
    res = [[None]*len(temp[i]) for i in range(len(temp))]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            res[i][len(temp[i])-1-j] = temp[j][i]
    return "\n".join(("".join(i) for i in res))


def diag_1_sym(s):
    temp = s.split("\n")
    res = [[None]*len(temp[i]) for i in range(len(temp))]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            res[i][j] = temp[j][i]
    return "\n".join(("".join(i) for i in res))


def selfie_and_diag1(s):
    res = []
    temp = s.split("\n")
    temp2 = diag_1_sym(s).split("\n")
    for i in range(len(temp)):
        res.append(f"{temp[i]}|{temp2[i]}")
    return "\n".join(("".join(i) for i in res))


def oper(fct, s):
    return fct(s)
