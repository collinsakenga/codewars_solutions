movement=[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def find_word(board, word):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==word[0] and helper(board, word[1:], i, j, {(i, j):1})==True:
                return True
    return False
def helper(board, word, y, x, memo):
    if word=="":
        return True 
    temp=[(y+i, x+j) for i,j in movement if valid(board, y+i, x+j) and board[y+i][x+j]==word[0] and memo.get((y+i, x+j))==None] 
    return any(helper(board, word[1:], i, j, {**memo, **{(i, j):1}}) for i,j in temp)
def valid(board, i, j):
    if (i<0 or j<0 or i>=len(board) or j>=len(board[0])):
        return False
    return True