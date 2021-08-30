def who_is_winner(pieces_position_list):
    rec=[i.split("_") for i in pieces_position_list]
    players=[rec[0][1],rec[1][1]]
    grid=[[" "]*7 for i in range(6)]
    check=[0 for i in range(7)]
    count=0
    while count<len(rec):
        player=players[count%2]    
        placement=ord(rec[count][0])-ord("A")
        check[placement]+=1
        count+=1
        if player=="Yellow":
            grid[6-check[placement]][placement]="O"
        elif player=="Red":
            grid[6-check[placement]][placement]="X"
        if win(grid):
            return player
    return "Draw"
def win(grid):
    for i in range(0,6):
        for j in range(0,4):
            if (grid[i][j]==grid[i][j+1]==grid[i][j+2]==grid[i][j+3]):
                if (grid[i][j]!=" "):
                    return True
    for i in range(0,7):
        for j in range(0,3):
            if (grid[j][i]==grid[j+1][i]==grid[j+2][i]==grid[j+3][i]):
                if (grid[j][i]!=" "):
                    return True
    for i in range(0,3):
        for j in range(0,4):
            if (grid[i][j]==grid[i+1][j+1]==grid[i+2][j+2]==grid[i+3][j+3]):
                if (grid[i][j]!=" "):
                    return True
    for i in range(5,1,-1):
        for j in range(0,4):
            if (grid[i][j]==grid[i-1][j+1]==grid[i-2][j+2]==grid[i-3][j+3]):
                if (grid[i][j]!=" "):
                    return True
    return False