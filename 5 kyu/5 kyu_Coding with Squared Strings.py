def code(s):
    if not s:
        return ""
    square = int(len(s)**0.5)+1 if str(len(s) **
                                       0.5)[-2:] != ".0" else int(len(s)**0.5)
    s = s+(square**2-len(s))*chr(11)
    temp = [s[square*i+j] for i in range(square) for j in range(square)]
    temp = [temp[i:i+square] for i in range(0, len(s), square)]
    res = [[""]*square for i in range(square)]
    for i in range(len(res)):
        for j in range(len(res)):
            res[i][j] = temp[square-1-j][i]
    return "\n".join(["".join(i) for i in res])


def decode(s):
    if not s:
        return ""
    temp = [list(i) for i in s.split("\n")]
    res = [[""]*len(temp[i]) for i in range(len(temp))]
    for i in range(len(res)):
        for j in range(len(res)):
            res[j][i] = temp[i][len(temp)-1-j]
    return "".join(["".join(i) for i in res]).rstrip(chr(11))
