def string_parse(string):
    if not isinstance(string, str):
        return "Please enter a valid string"
    temp=""
    res=""
    for i in string:
        temp+=i
        if temp[0]!=temp[-1]:
            res+=temp[:-1][:2]
            if len(temp[:-1])>2:
                res+="["+temp[:-1][2:]+"]"
            temp=i
    return res+temp if len(temp)<=2 else res+temp[:2]+"["+temp[2:]+"]"