def dec2FactString(nb):
    gen_fact()
    for i, j in enumerate(res):
        if j > nb:
            index = i-1
            break
    string = ""
    while index >= 0:
        string += key[nb//res[index]]
        nb -= nb//res[index]*res[index]
        index -= 1
    return string


def factString2Dec(string):
    gen_fact()
    total = 0
    for i, j in enumerate(string):
        total += key.index(j)*res[len(string)-1-i]
    return total


def gen_fact():
    if not res:
        temp = 1
        res.append(temp)
        for i in range(1, 36+2):
            temp *= i
            res.append(temp)
