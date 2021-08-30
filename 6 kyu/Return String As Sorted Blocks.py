from collections import Counter
def blocks(s):
    temp=Counter(s)
    res=[]
    while temp:
        string=""
        for i,j in temp.copy().items():
            string+=i
            temp[i]-=1
            if temp[i]<=0:
                del temp[i]
        res.append("".join(sorted(string, key=lambda x: rule(x))))
    return "-".join(res)
def rule(char):
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".index(char)
    