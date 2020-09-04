def string_transformer(s):
    temp = s[::-1]
    index = 0
    store = ""
    res = ""
    while index < len(temp):
        space = 0
        if temp[index] == " ":
            while index < len(temp):
                if temp[index] == " ":
                    index += 1
                    space += 1
                else:
                    break
            res += store[::-1]+space*" "
            store = ""
        else:
            store += temp[index].swapcase()
            index += 1
    res += store[::-1]
    return res
