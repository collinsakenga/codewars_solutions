def smallest(n):
    temp = list(str(n))
    smallest = 10
    for i in range(1, len(temp)):
        smallest = min(smallest, int(temp[i]))
        if smallest == int(temp[i]):
            index = i
    if int(temp[1]) == smallest:
        if temp[1:].count(str(smallest)) >= 2 and int(temp[0]) <= int(temp[2]):
            res = "".join(temp[index])+"".join(temp[0:index]
                                               )+"".join(temp[index+1:])
            while True:
                if int(temp[index-1]) != int(temp[index]):
                    break
                index -= 1
            return [int(res), index, 0]
        for i in range(2, len(temp)):
            if int(temp[0]) < int(temp[i]):
                index = i
                while True:
                    if int(temp[index-1]) != int(temp[index]):
                        break
                    index -= 1
                res = "".join(temp[1:index])+temp[0]+"".join(temp[index:])
                return [int(res), 0, index-1]
        res = "".join(temp[1:len(temp)])+temp[0]
        return [int(res), 0, len(temp)-1]
    for i in range(0, len(temp)):
        if smallest <= int(temp[i]):
            index2 = i
            break
    while True:
        if int(temp[index-1]) != int(temp[index]):
            break
        index -= 1
    res = "".join(temp[:index2])+temp[index] + \
        "".join(temp[index2:index])+"".join(temp[index+1:])
    return [int(res), index, index2]
