def ant(grid, column, row, n, direction = 0):
    for i in range(n):
        if grid[row][column]==0:
            direction=(direction-1)%4       
            grid[row][column]=1
        elif grid[row][column]==1:
            direction=(direction+1)%4
            grid[row][column]=0
        if direction==0:
            row-=1
            if row<0:
                grid.insert(0, [0]*len(grid[0]))
                row=0
        elif direction==1:
            column+=1
            if column>=len(grid[row]):
                for j in range(len(grid)):
                    grid[j].append(0)
        elif direction==2:
            row+=1
            if row>=len(grid):
                grid.append([0]*len(grid[0]))
        elif direction==3:
            column-=1
            if column<0:
                for j in range(len(grid)):
                    grid[j].insert(0, 0)
                column=0
    return grid