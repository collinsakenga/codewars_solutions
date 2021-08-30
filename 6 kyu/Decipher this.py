def decipher_this(string):
    temp=""
    res=""
    for word in string.split(" "):
        for i in word:
            try:
                c=int(i)
                temp+=i
            except:
                break                
        if len(temp)==len(word):
            res+=chr(int(temp))+" "
        elif len(temp)+1==len(word):
            res+=chr(int(temp))+word[-1]+" "
        else:
            res+=chr(int(temp))+word[-1]+word[len(temp)+1:-1]+word[len(temp)]+" "
        temp=""
    return res[:-1]