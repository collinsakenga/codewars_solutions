dict={ "A":"T", "G":"C", "T":"A", "C":"G"}
def translate_with_frame(s, frames=[1,2,3,-1,-2,-3]):
    if not frames:
        return []
    res=[]
    for i in frames:
        if i==1:
            res.append(one(s))
        elif i==2:
            res.append(two(s))
        elif i==3:
            res.append(three(s))
        elif i==-1:
            res.append(neg_one(s))
        elif i==-2:
            res.append(neg_two(s))
        elif i==-3:
            res.append(neg_three(s))
    return res
def one(s):
    res=[]
    for i in range(0, len(s), 3):
        res.append(s[i:i+3])
    for i,j in enumerate(res):
        res[i]=codons.get(j, "")
    return "".join(res)
def two(s):
    res=[]
    for i in range(1, len(s), 3):
        res.append(s[i:i+3])
    for i,j in enumerate(res):
        res[i]=codons.get(j, "")
    return "".join(res)
def three(s):
    res=[]
    for i in range(2, len(s), 3):
        res.append(s[i:i+3])
    for i,j in enumerate(res):
        res[i]=codons.get(j, "")
    return "".join(res)
def neg_one(s):
    temp=""
    for i in s:
        temp+=dict[i]
    temp=temp[::-1]
    res=[]
    for i in range(0, len(temp), 3):
        res.append(temp[i:i+3])
    for i,j in enumerate(res):
        res[i]=codons.get(j, "")
    return "".join(res)
def neg_two(s):
    temp=""
    for i in s:
        temp+=dict[i]
    temp=temp[::-1]
    res=[]
    for i in range(1, len(temp), 3):
        res.append(temp[i:i+3])
    for i,j in enumerate(res):
        res[i]=codons.get(j, "")
    return "".join(res)
def neg_three(s):
    temp=""
    for i in s:
        temp+=dict[i]
    temp=temp[::-1]
    res=[]
    for i in range(2, len(temp), 3):
        res.append(temp[i:i+3])
    for i,j in enumerate(res):
        res[i]=codons.get(j, "")
    return "".join(res)
def general(s):
    pass
def neg_general(s):
    pass