class keyword_cipher(object):
    def __init__(self, abc, keyword):
        self.word=abc
        self.key=""
        for i in keyword+abc:
            if not (i in self.key):
                self.key+=i
    def encode(self, plain):
        res=""
        for i in plain:
            res+=self.key[self.word.index(i)] if i in self.word else i
        return res
    def decode(self, ciphered):
        res=""
        for i in ciphered:
            res+=self.word[self.key.index(i)] if i in self.key else i
        return res