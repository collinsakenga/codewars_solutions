def vowel_back(st):
    res=""
    for i in st:
        if i in "aiu":
            temp=chr(ord("a")+(ord(i)-ord("a")-5)%26)
            res+=i if temp in "code" else temp
        elif i =="c" or i=="o":
            res+=chr(ord("a")+(ord(i)-ord("a")-1)%26)
        elif i=="d" or i=="e":
            res+="a"
        else:
            temp=chr(ord("a")+(ord(i)-ord("a")+9)%26)
            res+=i if temp in "code" else temp
    return res