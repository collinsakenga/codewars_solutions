def bears(x,s):
    hash=[True]*len(s)
    res=""
    for i in range(len(s)-1):
        if hash[i] and hash[i+1] and (s[i:i+2]=="B8" or s[i:i+2]=="8B"):
            res+=s[i:i+2]
            hash[i]=False
            hash[i+1]=False
    return [res, x*2<=len(res)]