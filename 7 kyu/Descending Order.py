def descending_order(s):
    s2=str(s)
    c=[]
    for i in range(len(s2)):
        c.append(s2[i])
    c.sort(reverse=True)
    s3=int(("".join(c)))
    return s3