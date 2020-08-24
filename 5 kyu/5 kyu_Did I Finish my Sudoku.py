def done_or_not(board):  # board[i][j]
    for row in range(0, len(board)):
        if len(set(board[row])) != 9:
            return 'Try again!'
    temp = []
    for row in range(0, 9):
        for col in range(0, 9):
            temp.append(board[col][row])
        if len(set(temp)) != 9:
            return 'Try again!'
        temp = []
    index1 = 0
    index2 = 0
    while True:
        try:
            for k in range(3):
                for l in range(3):
                    for i in range(3):
                        for j in range(3):
                            temp.append(board[index1+i][index2+j])
                    if len(set(temp)) != 9:
                        return "Try again!"
                    temp = []
                    index2 += 3
                index1 += 3
                index2 = 0
        except:
            return "Finished!"
