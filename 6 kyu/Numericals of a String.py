def numericals(s):
    temp=""
    res=""
    dict={}
    for c in s:
        try:
            dict[c]+=1
        except:
            dict[c]=1
        res+=f"{dict[c]}"
        temp+=c
    return res