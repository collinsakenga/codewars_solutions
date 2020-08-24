def first_non_repeating_letter(string):
    result = []
    for char in string:
        if char not in result:
            result.append(char)
    result2 = result.copy()
    for char in result2:
        if char.isalpha():
            if string.count(char.upper())+string.count(char.lower()) > 1:
                result.remove(char)
    for char in result:
        if string.count(char) == 1:
            return char
    return ""
