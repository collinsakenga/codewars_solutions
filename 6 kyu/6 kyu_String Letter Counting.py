def string_letter_count(string_sentence):
    a = 97
    string_letter = chr(a)
    string_sentence = string_sentence.lower()
    string_append = ""
    while string_letter < 'z':
        string_letter = chr(a)
        if string_sentence.count(string_letter) >= 1:
            string_append += str(int(string_sentence.count(string_letter))
                                 )+string_letter
        a += 1
    return(string_append)
