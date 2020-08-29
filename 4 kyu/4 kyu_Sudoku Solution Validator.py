def valid_solution(board):
    check = set()
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(i, i+3):
                for l in range(j, j+3):
                    check.add(board[k][l])
            if len(check) != 9:
                return False
            check.clear()
    for i in range(9):
        for j in range(9):
            check.add(board[i][j])
        if len(check) != 9:
            return False
        check.clear()
    for i in range(9):
        for j in range(9):
            check.add(board[j][i])
        if len(check) != 9:
            return False
        check.clear()
    return True
