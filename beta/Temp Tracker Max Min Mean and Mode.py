class TempTracker:
    def __init__(self):
        self.hash=[0]*111
        self.max=0
        self.min=110
        self.sum=0
        self.length=0
        self.mode=0
    def insert(self, temperature):
        self.max=max(temperature, self.max)
        self.min=min(temperature, self.min)
        self.sum+=temperature
        self.length+=1
        self.hash[temperature]+=1
        self.mode=self.hash.index(max(self.hash))
    def get_max(self):
        return None if not self.length else self.max
    def get_min(self):
        return None if not self.length else self.min
    def get_mean(self):
        return None if not self.length else self.sum/self.length
    def get_mode(self):
        return None if not self.length else self.mode