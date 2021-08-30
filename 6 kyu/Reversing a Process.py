def decode(r):
    num=""
    for i in r:
        try:
            num+=str(int(i))
            r=r[1:]
        except:
            num=int(num)
            break
    if num%2==0: return "Impossible to decode" 
    res=""
    for char in r:
        letter=ord(char)-ord("a")
        for i in range(0,26):
            if (i*num)%26==letter:
                res+=chr(ord("a")+i)
    return res if len(res)==len(r) else"Impossible to decode"