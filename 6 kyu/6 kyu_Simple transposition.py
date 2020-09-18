def simple_transposition(text):
    res = ""
    for i in range(0, len(text), 2):
        res += text[i]
    for i in range(1, len(text), 2):
        res += text[i]
    return res
