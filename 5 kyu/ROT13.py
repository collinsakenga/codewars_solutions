def rot13(message):
    result=""
    for char in list(message):
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            char=chr((ord("A")+(ord(char)-ord("A")+13)%26))
        elif char in "abcdefghijklmnopqrstuvwxyz":  
            char=chr((ord("a")+(ord(char)-ord("a")+13)%26))
        result+=char
    return result
