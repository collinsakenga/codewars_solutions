def camelize(str):
    res = ""
    temp = ""
    for i in str:
        if i.isalnum():
            temp += i
        else:
            res += temp.capitalize()
            temp = ""
    if temp:
        res += temp.capitalize()
    return res
