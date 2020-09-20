from copy import deepcopy


def rot(s):
    reserve = [list(i) for i in s.split("\n")]
    res = deepcopy(reserve)
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] = reserve[len(reserve)-1-i][len(reserve[i])-1-j]
    return "\n".join(("".join(i) for i in res))


def selfie_and_rot(s):
    temp = s.split("\n")
    temp2 = rot(s).split("\n")
    res = [[None]*(len(temp[0])*2) for i in range(len(temp)*2)]
    for i in range(len(res)//2):
        for j in range(len(res[i])):
            res[i][j] = temp[i][j] if j < len(temp[i]) else "."
    for i in range(len(res)//2, len(res)):
        for j in range(len(res[i])):
            res[i][j] = temp2[i-len(temp2)][j-len(temp2[0])
                                            ] if j >= len(temp2[0]) else "."
    return "\n".join(("".join(i) for i in res))


def oper(fct, s):
    return fct(s)
