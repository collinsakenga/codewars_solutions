from itertools import cycle
def basic_encryption(word, pw):
    res=""
    for i,j in enumerate(word):
        res+=chr((ord(j)+ord(pw[i%len(pw)]))//2)
    for i in range(len(word), len(pw)):
        res+=chr((ord(pw[i])+40)//2)
    return res