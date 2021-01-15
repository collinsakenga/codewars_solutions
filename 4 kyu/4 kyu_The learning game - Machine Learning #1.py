class Machine:
    def __init__(self):
        self.commands=list(ACTIONS())
        self.index=0
    def command(self, cmd, num):
        self.index+=1
        return self.commands[(self.index-1)%len(self.commands)](num)
    def response(self,res):
        if res==False:
            self.commands.pop((self.index-1)%len(self.commands))
            self.index=0