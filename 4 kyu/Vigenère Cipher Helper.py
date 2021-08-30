class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key=key
        self.alphabet=alphabet
        self.mod=len(key)
        self.alphabetLen=len(alphabet)
    def encode(self, text):
        temp=""
        for i in range(0, len(text)):
            if text[i] in self.alphabet:
                temp += self.alphabet[(self.alphabet.index(text[i])+self.alphabet.index(self.key[i % self.mod]))%self.alphabetLen]
            else:
                temp += text[i]
        return temp
    
    def decode(self, text):
        temp = ""
        for i in range(0, len(text)):
            if text[i] in self.alphabet:
                temp += self.alphabet[(self.alphabet.index(text[i])-self.alphabet.index(self.key[i % self.mod]))%self.alphabetLen]
            else:
                temp += text[i]
        return temp   