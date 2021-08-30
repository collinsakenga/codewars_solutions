class MList(list):
    def __init__(self, arr):
        self.list=arr
    def __add__(self, arr):
        res={i+j for i in self.list for j in arr}
        return sorted(res)
