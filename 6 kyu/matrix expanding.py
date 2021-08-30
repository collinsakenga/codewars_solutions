def expand(maze, fill):
    length=len(maze)
    res=[[fill]*(length*2) for i in range(length*2)]
    for i in range(length//2, length//2+length):
        for j in range(length//2, length//2+length):
            res[i][j]=maze[i-length//2][j-length//2]
    return res