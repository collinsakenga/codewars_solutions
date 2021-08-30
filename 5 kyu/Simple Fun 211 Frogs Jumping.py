def frogs_jumping(stones):
    check=set(stones)
    cur=stones[-1]
    res=[]
    while cur>0:
        if (cur-2) in check:
            res.append("2")
            cur-=2
        else:
            res.append("1")
            cur-=1
    return "".join(res)[::-1]