def pattern(n):
    if n<=0:
        return ""
    res=[["0"]*n for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            res[i][j]=str((n-i)%10)
            res[j][i]=str((n-i)%10)
    return "\n".join(["".join(i) for i in res])
