def look_and_say(data='1', maxlen=5):
    string=data
    res=[]
    for _ in range(maxlen):
        temp2=""
        temp="" 
        for i in range(len(string)):
            if not temp or string[i] in temp:
                temp+=string[i]
            else:
                temp2+=str(temp.count(temp[0]))+temp[0]
                temp=string[i]        
        temp2+=str(temp.count(temp[0]))+temp[0]     
        string=temp2
        res.append(string)     
    return res