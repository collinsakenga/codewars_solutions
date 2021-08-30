class DefaultList:
    def __init__(self, arr, item):
        self.list=arr
        self.default=item
    def __getitem__(self, i):
        try:
            return self.list[i]
        except:
            return self.default
    def append(self, item):
        self.list.append(item)
    def extend(self, item):
        self.list.extend(item)
    def remove(self, item):
        self.list.remove(item)
    def insert(self, index, item):
        self.list.insert(index, item)
    def pop(self, index):
        self.list.pop(index)