class Cipher(object):
    def __init__(self, map1, map2):
        self.trans=str.maketrans(map1,map2)
        self.trans2=str.maketrans(map2,map1)
    def encode(self, s):
        return s.translate(self.trans)
    
    def decode(self, s):
        return s.translate(self.trans2)