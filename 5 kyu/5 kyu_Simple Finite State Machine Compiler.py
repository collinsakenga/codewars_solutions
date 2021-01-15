class FSM(object):
    def __init__(self, instructions):
        self.result={}
        self.instructions={}
        for i in instructions.split("\n"):
            temp=i.split("; ")
            self.result[temp[0]]=int(temp[-1])
            self.instructions[temp[0]]=temp[1].split(", ")
    
    def run_fsm(self, start, sequence):
        path=[start]
        for i in sequence:
            path.append(self.instructions[path[-1]][i])
        return (path[-1], self.result[path[-1]], path)