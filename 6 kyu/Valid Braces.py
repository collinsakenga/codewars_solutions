def validBraces(string):
    temp=list(string)
    while temp:
        res=len(temp)
        for i in range(0,len(temp)-1):
            if (temp[i]=="(" and temp[i+1]==")" ) or (temp[i]=="[" and temp[i+1]=="]" ) or (temp[i]=="{" and temp[i+1]=="}" ):
                temp=temp[:i]+temp[i+2:]
                break
        if len(temp)==res:
            return False
    return True
        