def solution(word):
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
