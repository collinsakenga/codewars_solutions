movement=[(1, 0), (-1, 0), (0, 1), (0, -1)]
class Game():   
    def __init__(self, board):
        self.board=board
    def play(self):
        memo, dict={}, {}
        for i,j in enumerate(self.board):
            for k,l in enumerate(j):
                if l!=0 and (i,k) not in memo:
                    neighbours=self.helper(self.board, i, k, l, {})
                    dict[tuple((key for key in neighbours.keys()))]=l
                    for key in neighbours.keys():
                        memo[key]=1
        return len(dict)
    def helper(self, board, y, x, value, record):
        if record.get((y, x), None)!=None:
            return 
        record[(y, x)]=value
        for i,j in movement:
            if self.valid(board, y+i, x+j) and board[y+i][x+j]==value:
                self.helper(board, y+i, x+j, value, record)
        return record
    def valid(self, board, i, j):
        if (i<0 or j<0 or i>=len(board) or j>=len(board[0])):
            return False
        return True  