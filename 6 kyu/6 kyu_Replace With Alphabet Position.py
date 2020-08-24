def alphabet_position(sentence):
    empty_string = ""
    sentence = sentence.lower()
    for char in sentence:
        if ord(char) >= 97 and ord(char) <= 122:
            empty_string += " "+str(ord(char)-96)
    return(empty_string[1:])
