def shifted_diff(first, second):
    if len(first) != len(second):
        return -1
    if len(first) <= 1:
        return 0
    count = 0
    loop = len(first)
    s = second
    temp = first
    while count < loop:
        if temp == second:
            return count
        s = temp[-1]+temp[:-1]
        temp = s
        count += 1
    return -1
