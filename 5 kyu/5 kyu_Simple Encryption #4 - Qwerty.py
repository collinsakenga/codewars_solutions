key1 = "qwertyuiop"
key2 = "asdfghjkl"
key3 = "zxcvbnm,."
key1_upper = key1.upper()
key2_upper = key2.upper()
key3_upper = "ZXCVBNM<>"


def encrypt(text, encryptKey):
    return cipher(text, encryptKey, 1)


def decrypt(text, encryptKey):
    return cipher(text, encryptKey, -1)


def cipher(text, encryptKey, flag):
    res = ""
    for i in text:
        if i in key1:
            res += key1[(key1.index(i)+flag*(encryptKey//100)) % len(key1)]
        elif i in key2:
            res += key2[(key2.index(i)+flag*(encryptKey//10 % 10)) % len(key2)]
        elif i in key3:
            res += key3[(key3.index(i)+flag*(encryptKey % 10)) % len(key3)]
        elif i in key1_upper:
            res += key1_upper[(key1_upper.index(i)+flag *
                               (encryptKey//100)) % len(key1_upper)]
        elif i in key2_upper:
            res += key2_upper[(key2_upper.index(i)+flag *
                               (encryptKey//10 % 10)) % len(key2_upper)]
        elif i in key3_upper:
            res += key3_upper[(key3_upper.index(i)+flag *
                               (encryptKey % 10)) % len(key3_upper)]
        else:
            res += i
    return res
