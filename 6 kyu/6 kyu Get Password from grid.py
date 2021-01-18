def get_password(grid,directions):
    pw=""
    x=y=0
    limitx=len(grid[0])
    limity=len(grid)
    for i,j in enumerate(grid):
        for k,l in enumerate(j):
            if l=="x":
                y=i
                x=k
                break
    for i in directions:
        if "right" in i:
            x+=1 if x!=limitx-1 else -(limitx-1)
        elif "down" in i:
            y+=1 if y!=limity-1 else -(limity-1)
        elif "left" in i:
            x-=1 if x!=0 else -(limitx-1)
        elif "up" in i:
            y-=1 if y!=0 else -(limity-1)
        if "T" in i:
            pw+=grid[y][x]
    return pw