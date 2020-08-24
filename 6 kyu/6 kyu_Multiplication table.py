def multiplication_table(size):
    temp = [i+1 for i in range(size)]
    temp2 = temp.copy()
    res = []
    res.append(temp2)
    for i in range(1, size):
        for j in range(0, len(temp)):
            temp[j] += temp2[j]
        temp3 = temp.copy()
        res.append(temp3)
    return res
