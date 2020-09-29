def x(n):
    res = [[None]*n for i in range(n)]
    for i in range(len(res)):
        for j in range(len(res[i])):
            if i == j:
                res[i][j] = "■"
            elif (i+j) == (n-1):
                res[i][j] = "■"
            else:
                res[i][j] = "□"
    return "\n".join("".join(i) for i in res)
