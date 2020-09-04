def decodeMorse(morse_code):
    string = []
    res = morse_code.split("   ")
    for i in res:
        temp = ""
        for j in i.split():
            temp += MORSE_CODE[j]
        string.append(temp)
    return " ".join(string).lstrip()
