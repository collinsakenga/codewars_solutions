def one_down(txt):
    if not isinstance(txt, str):
        return "Input is not a string"
    res=""
    for i in txt:
        if i.isupper():
            res+=chr(ord("A")+(ord(i)-ord("A")-1)%26)
        elif i.islower():
            res+=chr(ord("a")+(ord(i)-ord("a")-1)%26)
        else:
            res+=i
    return res