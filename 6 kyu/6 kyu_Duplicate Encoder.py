def duplicate_encode(word):
    result = ""
    word = word.lower()
    # case insensitive
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("
    return result
