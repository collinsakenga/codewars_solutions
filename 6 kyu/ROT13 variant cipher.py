def encrypter(strng):
    res=""
    for i in strng:
        res+=chr(ord("a")+(ord(i)-ord("a")+13)%26) if i.isalpha() else i
    return res.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"))