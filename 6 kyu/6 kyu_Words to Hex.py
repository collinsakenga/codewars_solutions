def words_to_hex(words):
    return [hex_words(i) for i in words.split()]


def hex_words(s):
    res = ""
    for i in s[:3]:
        res += str(hex(ord(i))[2:])
    return "#"+res.ljust(6, "0")
