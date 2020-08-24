def maze_runner(maze, directions):
    flag = False
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == 2:
                y = i
                x = j
                flag = True
                break
        if flag:
            break
    for i in range(0, len(directions)):
        try:
            if directions[i] == "N":
                if y-1 < 0:
                    return "Dead"
                if maze[y-1][x] == 1:
                    return "Dead"
                elif maze[y-1][x] == 3:
                    return "Finish"
                else:
                    y -= 1
            elif directions[i] == "E":
                if maze[y][x+1] == 1:
                    return "Dead"
                elif maze[y][x+1] == 3:
                    return "Finish"
                else:
                    x += 1
            elif directions[i] == "S":
                if maze[y+1][x] == 1:
                    return "Dead"
                elif maze[y+1][x] == 3:
                    return "Finish"
                else:
                    y += 1
            elif directions[i] == "W":
                if x-1 < 0:
                    return "Dead"
                if maze[y][x-1] == 1:
                    return "Dead"
                elif maze[y][x-1] == 3:
                    return "Finish"
                else:
                    x -= 1
        except:
            return "Dead"
    return "Lost"
