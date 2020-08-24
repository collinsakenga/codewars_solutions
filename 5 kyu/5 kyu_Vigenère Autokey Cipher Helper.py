class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.alphabet = abc
        self.alphabetLen = len(abc)
        self.mod = len(key)

    def encode(self, text):
        temp = ""
        temp2 = ""
        for i in range(0, len(text)):
            if text[i] in self.alphabet:
                if len(temp2) < len(self.key):
                    temp += self.alphabet[(self.alphabet.index(text[i])+self.alphabet.index(
                        self.key[len(temp2)])) % self.alphabetLen]
                else:
                    temp += self.alphabet[(self.alphabet.index(text[i])+self.alphabet.index(
                        temp2[len(temp2)-self.mod])) % self.alphabetLen]
                temp2 += text[i]
            else:
                temp += text[i]
        return temp

    def decode(self, text):
        temp = ""
        temp2 = ""
        for i in range(0, len(text)):
            if text[i] in self.alphabet:
                if len(temp2) < len(self.key):
                    temp += self.alphabet[(self.alphabet.index(text[i])-self.alphabet.index(
                        self.key[len(temp2)])) % self.alphabetLen]
                else:
                    temp += self.alphabet[(self.alphabet.index(text[i])-self.alphabet.index(
                        temp2[len(temp2)-self.mod])) % self.alphabetLen]
                temp2 += temp[i]
            else:
                temp += text[i]
        return temp
