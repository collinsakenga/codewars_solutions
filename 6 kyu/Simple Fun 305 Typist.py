def typist(s):
    cur=res=0
    for i in s:
        next_val=int(i.isupper())
        res+=1+int(next_val!=cur)
        cur=next_val
    return res