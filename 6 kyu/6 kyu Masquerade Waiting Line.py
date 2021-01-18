def friend_find(line):
    check=[i for i,j in enumerate(line) if j=="red"]
    total=0
    for i in check:
        if i>=2 and line[i-1]=="blue" and line[i-2]=="blue":
            total+=1
        elif (i>=1 and i<=len(line)-2) and line[i-1]=="blue" and line[i+1]=="blue":
            total+=1
        elif (i<=len(line)-3) and line[i+1]=="blue" and line[i+2]=="blue":
            total+=1
    return total