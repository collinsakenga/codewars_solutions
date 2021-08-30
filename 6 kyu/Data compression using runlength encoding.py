def encode(string):
    res=""
    temp=""
    for i in string:
        temp+=i
        if len(set(temp))==2:
            temp=temp[:-1]
            res+=f"{len(temp)}{temp[0]}"
            temp=i
    if temp:
        res+=f"{len(temp)}{temp[0]}"
    return res
def decode(string): 
    res=""
    temp=""
    for i in string:
        if i.isdigit():
            temp+=i
        else:
            res+=int(temp)*i
            temp=""
    return res