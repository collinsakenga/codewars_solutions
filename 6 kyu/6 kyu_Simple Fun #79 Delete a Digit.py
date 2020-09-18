def delete_digit(n):
    temp = list(str(n))
    s = str(n)
    flag = True
    for i in range(len(s)-1):
        if int(s[i+1]) > int(s[i]):
            remove = i
            flag = False
            break
    if flag:
        temp.pop()
        return int("".join(temp))
    temp.pop(remove)
    return int("".join(temp))
