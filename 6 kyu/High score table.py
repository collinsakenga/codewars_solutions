class HighScoreTable:
    
    def __init__(self, n):
        self.scores=[]
        self.limit=n
    
    def update(self, n):
        if len(self.scores)<self.limit:
            self.scores.append(n)
            self.scores.sort(reverse=True)
        elif n>min(self.scores):
            self.scores.remove(min(self.scores))
            self.scores.append(n)
            self.scores.sort(reverse=True)   
    def reset(self):
        self.scores=[]