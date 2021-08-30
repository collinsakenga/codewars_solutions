def min_path(grid, x, y):
    res=[[None]*len(grid[i]) for i in range(len(grid))]
    for i in range(y, -1, -1):
        for j in range(x, -1, -1):
            if i==y and j==x:
                res[i][j]=grid[i][j]
            elif i==y:
                res[i][j]=grid[i][j]+res[i][j+1]
            elif j==x:
                res[i][j]=grid[i][j]+res[i+1][j]
            else:
                res[i][j]=grid[i][j]+min(res[i+1][j], res[i][j+1])
    return res[0][0]