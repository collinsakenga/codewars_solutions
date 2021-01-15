from copy import deepcopy
from math import ceil
class Sudoku(object):
    def __init__(self, data):
        self.data=deepcopy(data)
        self.limit=len(data)
    def is_valid(self):
        if self.limit!=len(self.data[0]) or any((not isinstance(j, int) or isinstance(j, bool) or j<=0 or j>self.limit) for i in self.data for j in i):
            return False
        for i in range(self.limit):
            temp1=set()
            temp2=set()
            for j in range(self.limit):
                temp1.add(self.data[i][j])
                temp2.add(self.data[j][i])
            if len(temp1)!=self.limit or len(temp2)!=self.limit:
                return False
        square=ceil(self.limit**0.5)
        for i in range(0, self.limit, square):
            for j in range(0, self.limit, square):
                temp3=set()
                for k in range(i ,i+square):
                    for l in range(j, j+square):
                        temp3.add(self.data[k][l])
                if len(temp3)!=self.limit:
                    return False
        return True