def corner_fill(square):
    if not square:
        return []
    res=[square[-1][0]]
    y, x=len(square)-1, 0
    size=(y+1)**2
    move=1
    if len(square)%2:
        while len(res)<size:
            y-=1
            if y>=0:
                res.append(square[y][x])
                for i in range(x+1, x+move+1):
                    res.append(square[y][i])
                x+=move
                for i in range(y+1, y+move+1):
                    res.append(square[i][x])
                y+=move
            move+=1
            x+=1
            if x<len(square):
                res.append(square[y][x])
                for i in range(y-1, y-1-move, -1):
                    res.append(square[i][x])
                y-=move
                for i in range(x-1, x-1-move, -1):
                    res.append(square[y][i])
                x-=move
            move+=1
    else:
        while len(res)<size:
            x+=1
            if x<len(square):
                res.append(square[y][x])
                for i in range(y-1, y-1-move, -1):
                    res.append(square[i][x])
                y-=move
                for i in range(x-1, x-1-move, -1):
                    res.append(square[y][i])
                x-=move
            move+=1
            y-=1
            if y>=0:
                res.append(square[y][x])
                for i in range(x+1, x+move+1):
                    res.append(square[y][i])
                x+=move
                for i in range(y+1, y+move+1):
                    res.append(square[i][x])
                y+=move
            move+=1
    return res[::-1]
    '''
    urdrul
    111122133144
    '''