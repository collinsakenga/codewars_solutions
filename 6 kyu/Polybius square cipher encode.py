def polybius(text):
    res=""
    for i in text:
        if i.isalpha():
            temp=ord(i)-ord("A")
            if ord(i)>=ord("J"):
                temp-=1
            res+=f"{temp//5+1}{temp%5+1}"
        else:
            res+=i
    return res