class RomanNumerals:
    def to_roman(self, num):
        rec = num
        res = ""
        if rec >= 1000:
            res += rec//1000*"M"
            rec -= rec//1000*1000
        if rec >= 900:
            res += "CM"
            rec -= 900
        if rec >= 500:
            res += "D"
            rec -= 500
        if rec >= 400:
            res += "CD"
            rec -= 400
        if rec >= 100:
            res += rec//100*"C"
            rec -= rec//100*100
        if rec >= 90:
            res += "XC"
            rec -= 90
        if rec >= 50:
            res += "L"
            rec -= 50
        if rec >= 40:
            res += "XL"
            rec -= 40
        if rec >= 10:
            res += rec//10*"X"
            rec -= rec//10*10
        if rec >= 9:
            res += "IX"
            rec -= 9
        if rec >= 5:
            res += "V"
            rec -= 5
        if rec >= 4:
            res += "IV"
            rec -= 4
        if rec >= 1:
            res += rec*"I"
        return res

    def from_roman(self, word):
        dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
                "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        num = 0
        while len(word) > 0:
            if len(word) >= 2:
                if word[0:2] in dict:
                    num += dict[word[0:2]]
                    word = word[2:]
                    continue
            num += dict[word[0:1]]
            word = word[1:]
        return num
