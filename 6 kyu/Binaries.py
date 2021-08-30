def code(strng):
    res=""
    for i in strng:
        temp=bin(int(i))[2:]
        res+=(len(temp)-1)*"0"+"1"+temp
    return res
def decode(strng):
    res=""
    index=0
    while strng:
        if strng[index]=="1":
            res+=str(int(strng[index+1:index+1+(index+1)], 2))
            strng=strng[index+1+(index+1):]
            index=0
            continue
        index+=1    
    return res