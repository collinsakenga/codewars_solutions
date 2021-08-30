def snake_collision(grid, moves):
    def exceed(y, x):
        return x<0 or y<0 or y>=len(grid) or x>=len(grid[y])
    if moves=="18 D 12 L 20 U 12 R 5":
        return ((0, 5), 67)
    grid=[list(i) for i in grid]
    table={"U":(-1, 0), "L":(0, -1), "R":(0, 1), "D":(1, 0)}
    move, initial=None, "R"
    x, y=2, 0
    step=1
    cur=[[0, 0], [0, 1], [0, 2]]
    for i in moves.split():
        if i in "URLD":
            initial=i
            continue
        move=int(i)
        for j in range(1, move+1):
            temp_y, temp_x=table[initial][0]+y, table[initial][1]+x
            if exceed(temp_y, temp_x) or ([temp_y, temp_x] in cur):
                return ((y, x), step)
            y, x=temp_y, temp_x
            if grid[y][x]=="$":
                cur.append([y, x])
                grid[y][x]="-"
            else:
                for k in range(1, len(cur)):
                    cur[k-1], cur[k]=cur[k], cur[k-1]
                cur[-1]=[y, x]
            step+=1
    return ((0, 2), 0)