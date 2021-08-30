def vowel_shift(text,n):
    if not text or n==0:
        return text
    index=[j for i,j in enumerate(text) if j in "AEIOUaeiou"]
    index2=[i for i,j in enumerate(text) if j in "AEIOUaeiou"]
    if len(index)<=1:
        return text
    if n<0:
        for i in range(abs(n)%len(index)):
            index.append(index.pop(0))
    else:
        for i in range(n%len(index)):
            index.insert(0,index.pop())
    res=list(text)
    for i,j in enumerate(index):
        res[index2[i]]=j
    return "".join(res)
        