def group_by_commas(n):
    temp = list(str(n)[::-1])
    i = 1
    while i != len(temp):
        if i % 3 == 0:
            temp[i] = ","+temp[i]
        i += 1
    return "".join(temp)[::-1]
