class Plugboard(object):
    def __init__(self, wires=None):
        if wires and (len(wires)>20 or (len(set(wires))!=len(wires)) or len(wires)%2!=0):
            raise Exception()
        self.wires=wires if wires else ""              
    def process(self, c):
        temp=[self.wires[i:i+2] for i in range(0, len(self.wires), 2)]
        res="" 
        for i in c:
            if i not in self.wires:
                res+=i
            else:
                if self.wires.index(i)%2==0:
                    res+=temp[self.wires.index(i)//2][1]
                else:
                    res+=temp[self.wires.index(i)//2][0]
        return res