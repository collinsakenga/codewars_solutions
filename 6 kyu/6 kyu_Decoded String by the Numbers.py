def decode(str):
    if not str:
        return []
    index=0
    res=[]
    while index<len(str):
        if str[index]=="\\":
            while index<len(str) and str[index]=="\\":
                index+=1
            num=""
            while index<len(str) and str[index].isdigit():
                num+=str[index]
                index+=1
            temp=""
            for i in range(int(num)):
                if index+i>=len(str):
                    break
                temp+=str[index+i]
            index+=int(num)
            res.append(temp)
        else:
            res.append(str[index])
            index+=1
    return res