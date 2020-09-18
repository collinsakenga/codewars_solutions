def closest(strng):
    dict = {}
    rec = strng.split()
    for i in range(len(rec)):
        dict[i] = rec[i]
    temp = sorted(dict.items(), key=lambda x: (digitsum(x[1]), x[0]))
    if not temp:
        return temp
    diff = digitsum(temp[-1][1])
    for i in range(len(temp)-1):
        var1 = digitsum(temp[i][1])
        var2 = digitsum(temp[i+1][1])
        diff = min(var2-var1, diff)
        if var1 == var2:
            return [[var1, temp[i][0], int(temp[i][1])], [var2, temp[i+1][0], int(temp[i+1][1])]]
    for i in range(len(temp)-1):
        var1 = digitsum(temp[i][1])
        var2 = digitsum(temp[i+1][1])
        if (var2-var1) == diff:
            return [[var1, temp[i][0], int(temp[i][1])], [var2, temp[i+1][0], int(temp[i+1][1])]]


def digitsum(n):
    total = 0
    for i in n:
        total += int(i)
    return total
