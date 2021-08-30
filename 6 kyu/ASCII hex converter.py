class Converter():
    @staticmethod
    def to_ascii(h):
        res=""
        for i in range(0, len(h), 2):
            res+=chr(int(h[i:i+2], 16))
        return res
    @staticmethod
    def to_hex(s):
        res=""
        for i in s:
            res+=hex(ord(i))[2:]
        return res