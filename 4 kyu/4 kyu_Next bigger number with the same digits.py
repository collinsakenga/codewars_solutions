def next_bigger(n):
    print(n)
    flag = False
    for i in range(0, len(str(n))-1):
        if int(str(n)[i+1]) > int(str(n)[i]):
            flag = True
            break
    if not flag:
        return -1
    index = 1
    rec = n
    n = str(n)
    while index < len(n):
        temp = n[index:]
        for i in range(len(temp)-1):
            if int(temp[i]) < int(temp[i+1]):
                flag = False
                break
        if flag:
            break
        index += 1
        flag = True
    check = 9
    pre = n[:index]
    for i in temp:
        if int(i) > int(n[index-1]):
            check = min(int(i), check)
    first = pre[:-1]+str(check)
    second = temp[:temp.index(str(check))]+pre[-1] + \
        temp[temp.index(str(check))+1:]
    second = "".join(sorted(second))
    return int(first+second)
