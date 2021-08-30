def easy_cipher(text):
    temp="".join(text.lower().split())
    dict={'a': 'l', 'g': 'o', 'r': 'i', 't': 'h', 'm': 's', 'p': 'y','A': 'L', 'G': 'O', 'R': 'I', 'T': 'H', 'M': 'S', 'P': 'Y','l': 'a', 'o': 'g', 'i': 'r', 'h': 't', 's': 'm', 'y': 'p', 'L': 'A', 'O': 'G', 'I': 'R', 'H': 'T', 'S': 'M', 'Y': 'P'}
    res=""
    num=""
    for i in temp:
        if not i.isdigit():
            if num:
                res+=str(int(num)+100)
                num=""
            res+=dict[i] if i in dict else i
        else:
            num+=i
    if num:
        res+=str(int(num)+100)
    return res