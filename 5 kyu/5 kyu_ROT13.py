def rot13(message):
    result = ""
    for char in message:
        if char.isupper():
            char = chr((ord("A")+(ord(char)-ord("A")+13) % 26))
        elif char.islower():
            char = chr((ord("a")+(ord(char)-ord("a")+13) % 26))
        result += char
    return result
