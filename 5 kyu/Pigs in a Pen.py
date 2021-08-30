class Game():
    def __init__(self, board):
        self.board=board
    def play(self, lines):
        res=set(lines)
        length=self.board*2+1
        while True:
            record=len(res)
            for i in range(self.board):
                start=1+length*i
                for j in range(self.board):
                    top, bottom, left, right=start+j, start+length+j, start+j+self.board, start+j+self.board+1
                    top_here, bottom_here, left_here, right_here=top in res, bottom in res, left in res, right in res
                    if (top_here and bottom_here and left_here):
                        res.add(right)
                    elif (top_here and bottom_here and right_here):
                        res.add(left)
                    elif (bottom_here and left_here and right_here):
                        res.add(top)
                    elif (top_here and left_here and right_here):
                        res.add(bottom)
            if len(res)==record:
                break
        return sorted(res)