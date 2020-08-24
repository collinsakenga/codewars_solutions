def next_smaller(n):
    index = 1
    rec = str(n)
    flag = False
    for i in range(len(rec)-1):
        if int(rec[i+1]) < int(rec[i]):
            flag = True
            break
    if not flag:
        return -1
    while index < len(rec):
        temp = rec[index:]
        for i in range(len(temp)-1):
            if int(temp[i+1]) < int(temp[i]):
                flag = False
                break
        if flag:
            break
        flag = True
        index += 1
    check = -1
    rec2 = int(rec[:index][-1])
    for i in temp:
        if int(i) < rec2:
            check = max(check, int(i))
    first = rec[:index-1]+str(check)
    second = temp[:temp.index(str(check))] + \
        rec[:index][-1]+temp[temp.index(str(check))+1:]
    if first[0] == "0":
        return -1
    second = "".join(sorted(second, reverse=True))
    return int(first+second)
