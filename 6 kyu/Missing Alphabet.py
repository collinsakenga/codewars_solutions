def insert_missing_letters(st):
    alphabet=list("abcdefghijklmnopqrstuvwxyz")
    for i in set(st):
        alphabet.remove(i)
    if not alphabet:
        return st
    res=""
    for index,i in enumerate(st):
        if i in st[:index]:
            res+=i 
            continue
        letter=i.lower()
        flag=True
        while ord(letter)<=ord("z"):
            if letter in alphabet:
                res+=(i if i.islower() else i.upper())+"".join(j.upper() if i.islower() else j for j in alphabet[alphabet.index(letter):])
                flag=False
                break
            letter=chr(ord(letter)+1)
        if flag:
            res+=i
    return res