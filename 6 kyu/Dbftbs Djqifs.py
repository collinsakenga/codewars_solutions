def encryptor(key, message):
    res=""
    for i in message:
        if i.islower():
            res+=chr(ord("a")+(ord(i)-ord("a")+key)%26)
        elif i.isupper():
            res+=chr(ord("A")+(ord(i)-ord("A")+key)%26)
        else:
            res+=i
    return res