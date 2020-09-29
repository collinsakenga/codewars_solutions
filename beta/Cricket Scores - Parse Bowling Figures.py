from math import inf


class BowlingFigures:
    def __init__(self, figures):
        self.list = figures.split()
        self.index = 1
        while True:
            try:
                float(self.list[self.index])
                break
            except:
                self.index += 1
        self.name = " ".join(self.list[:self.index])
        self.overs = float(self.list[self.index])
        self.maidens = int(self.list[self.index+1])
        self.runs = int(self.list[self.index+2])
        self.wickets = int(self.list[self.index+3])
        temp = self.list[self.index].split(".")
        total = (6*int(temp[0])+int(temp[1]))
        self.economy = round(self.runs/(total/6), 2)
        self.strike_rate = inf if self.wickets == 0 else round(
            total/self.wickets, 2)
