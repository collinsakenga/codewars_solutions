def transpose(matrix):
    res = [[None]*len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] = matrix[j][i]
    return res
