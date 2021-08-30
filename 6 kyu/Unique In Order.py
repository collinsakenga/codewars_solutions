def unique_in_order(s):
    c=[]
    if len(s)>0:
        c=[s[0]]
    for i in range(len(s)-1):
        if s[i+1]!=s[i]:
            c.append(s[i+1])
    return c