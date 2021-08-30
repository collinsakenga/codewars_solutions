def caesar_encode(phrase, shift):
    res=[]
    for i,j in enumerate(phrase.split()):
        res.append("".join(chr(ord("a")+(ord(k)-ord("a")+shift+i)%26) for k in j))
    return " ".join(res)