class CaesarCipher(object):
    def __init__(self, shift):
        self.shift=shift
    def encode(self, st):
        temp=""
        for char in st:
            if char.islower():
                temp+=chr(ord("a")+((ord(char)-ord("a")+self.shift)%26))
            elif char.isupper():
                temp+=chr(ord("A")+((ord(char)-ord("A")+self.shift)%26))
            else:
                temp+=char
        return temp.upper()        
    def decode(self, st):
        temp=""
        for char in st:
            if char.islower():
                temp+=chr(ord("a")+((ord(char)-ord("a")-self.shift)%26))
            elif char.isupper():
                temp+=chr(ord("A")+((ord(char)-ord("A")-self.shift)%26))
            else:
                temp+=char
        return temp.upper()