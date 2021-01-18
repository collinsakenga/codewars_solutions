def mid_endian(n):
    temp=hex(n)[2:].upper()
    word=temp.rjust(len(temp)+len(temp)%2, "0")
    res=""
    mid=[word[i:i+2] for i in range(0, len(word), 2)]
    if len(mid)%2==1:
        for i in range(len(mid)-2, -1, -2):
            res+=mid[i]
        for i in range(0, len(mid), 2):
            res+=mid[i]
    else:
        for i in range(len(mid)-1, -1, -2):
            res+=mid[i]
        for i in range(0, len(mid), 2):
            res+=mid[i]
    return res