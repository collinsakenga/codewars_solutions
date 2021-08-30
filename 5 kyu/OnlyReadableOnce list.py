from copy import deepcopy
class SecureList():
    def __init__(self, l):
        self.list=[i for i in l]
    def __getitem__(self, index):
        temp=self.list[index]
        self.list.pop(index)
        return temp
    def __str__(self):
        temp=deepcopy(self.list)
        self.list.clear()
        return "["+", ".join(str(i) for i in temp)+"]"
    def __len__(self):
        return len(self.list)
    def __repr__(self):
        temp=deepcopy(self.list)
        self.list.clear()
        return str(temp)