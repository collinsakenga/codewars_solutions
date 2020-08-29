class SnakesLadders():

    def __init__(self):
        self.dict = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98,
                     87: 94, 16: 6, 49: 11, 46: 25, 62: 19, 64: 60, 74: 53, 89: 68, 99: 80, 95: 75, 92: 88}
        self.index = 0
        self.player = [1, 2]
        self.mark = [0, 0]
        self.win = False

    def play(self, die1, die2):
        if self.win:
            return 'Game over!'
        temp = self.index % 2
        record = self.mark[temp]
        self.mark[temp] += die1+die2
        if self.mark[temp] > 100:
            self.mark[temp] = record-die1-die2+(100-record)*2
        elif self.mark[temp] == 100:
            self.win = True
            return f"Player {self.player[temp]} Wins!"
        if self.mark[temp] in self.dict:
            self.mark[temp] = self.dict[self.mark[temp]]
        self.index += 1 if die1 != die2 else 0
        return f"Player {self.player[temp]} is on square {self.mark[temp]}"
