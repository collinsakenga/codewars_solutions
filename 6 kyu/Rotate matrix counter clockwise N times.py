from copy import deepcopy
def rotate_against_clockwise(matrix, times):
    count=times%4
    res=deepcopy(matrix)
    x=len(matrix[0])
    for _ in range(count):
        for i,j in enumerate(matrix):
            for k,l in enumerate(j):
                res[i][k]=matrix[k][x-1-i]
        matrix=deepcopy(res)
    return res