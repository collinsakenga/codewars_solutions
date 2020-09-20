def sum_arrays(array1, array2):
    if not array1 and not array2:
        return []
    elif not array1:
        return array2
    elif not array2:
        return array1
    temp = "".join(str(i) for i in array1)+"+"+"".join(str(i) for i in array2)
    if "-" in temp[1:]:
        temp = temp[:temp.index("+")]+temp[temp.index("+")+1:]
    temp = str(eval(temp))
    return [int(i) for i in temp] if temp[0] != "-" else [-int(j) if i == 0 else int(j) for i, j in enumerate(temp[1:])]
