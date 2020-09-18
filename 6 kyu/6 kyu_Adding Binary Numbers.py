def add(a, b):
    temp1 = a
    temp2 = b
    if len(temp1) > len(temp2):
        temp2 = "0"*(len(temp1)-len(temp2))+temp2
    else:
        temp1 = "0"*(len(temp2)-len(temp1))+temp1
    index = len(temp1)-1
    res = ""
    flag = False
    while index >= 0:
        if temp1[index] == "1" and temp2[index] == "1":
            check = 2
        elif temp1[index] == "0" and temp2[index] == "0":
            check = 0
        else:
            check = 1
        if flag:
            check += 1
        if check == 3:
            flag = True
            res = "1"+res
        elif check == 2:
            flag = True
            res = "0"+res
        elif check == 1:
            res = "1"+res
            flag = False
        else:
            res = "0"+res
            flag = False
        index -= 1
    if check >= 2:
        res = "1"+res
    return res.lstrip("0") if res.lstrip("0") else "0"
