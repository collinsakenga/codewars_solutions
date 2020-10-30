def rotate_clockwise(matrix):
    if not matrix:
        return []
    res = [[None]*len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] = matrix[len(matrix)-1-j][i]
    for i, j in enumerate(res):
        res[i] = "".join(j)
    return res
