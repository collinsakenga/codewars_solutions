class WordDictionary:
    def __init__(self):
        self.list=set()
    def add_word(self, word):
        self.list.add(word)
    def search(self, s):
        if s in self.list:
            return True
        for i in self.list:
            if len(i)!=len(s):
                continue
            flag=True
            for index,j in enumerate(s):
                if j==".":
                    continue
                if j!=i[index]:
                    flag=False
                    break
            if flag:
                return True
        return False