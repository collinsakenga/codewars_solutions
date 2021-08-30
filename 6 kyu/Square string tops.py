def tops(msg):
    total=3
    increment=7
    count=1
    res=""
    while total<len(msg):
        res=msg[total-1:total+count]+res
        total+=increment
        increment+=4
        count+=1
    return res