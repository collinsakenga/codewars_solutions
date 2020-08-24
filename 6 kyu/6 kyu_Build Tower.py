def tower_builder(num):
    c=[]
    s=""
    for row in range(0,num):
        for space in range(num-1,row,-1):
            s+=" "
        for star in range(0,row*2+1):
            s+="*"
        for space in range(num-1,row,-1):
            s+=" "
        c.append(s)
        s=""
    return c