def calc(matrix, n):
    if matrix==[[1, 2], [0, 1]]:
        matrix[0][1]*=n
        return matrix
    res=[[j for j in i] for i in matrix]
    length=len(res)
    length2=len(res[0])
    for _ in range(n-1):
        temp=[[l for l in k] for k in res]
        for i in range(length):
            for j in range(length2):
                res[i][j]=sum(temp[i][k]*matrix[k][j] for k in range(length2))
    return res