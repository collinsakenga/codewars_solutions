def display_board(board, width):
    res=[]
    for i in range(0, len(board), width):
        res.append("|".join((f" {i} " for i in board[i:i+width])))
        res.append("-"*(width*4-1))
    return "\n".join(res[:-1])