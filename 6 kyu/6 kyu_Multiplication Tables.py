def multiplication_table(row, col):
    result = []
    result2 = []
    temp = [0]*col
    for i in range(1, row+1):
        for j in range(1, col+1):
            temp[j-1] += j
        result.extend(temp)
        result2.append(result)
        result = []
    return result2
