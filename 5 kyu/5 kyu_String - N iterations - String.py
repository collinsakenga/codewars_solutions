def jumbled_string(s, n):
    total = len(s)-2 if len(s) % 2 == 0 else len(s)-1
    divide = len(s)//2-1 if len(s) % 2 == 0 else len(s)//2
    count = 0
    temp = total
    while True:
        if temp == total and count != 0:
            break
        if total % 2 == 0:
            total //= 2
        else:
            total = divide+(total+1)//2
        count += 1
    temp = list(s)
    count2 = 0
    res = ""
    while count2 < n % count:
        for i in range(0, len(temp), 2):
            res += temp[i]
        for i in range(1, len(temp), 2):
            res += temp[i]
        temp = list(res)
        res = ""
        count2 += 1
    return "".join(temp)
