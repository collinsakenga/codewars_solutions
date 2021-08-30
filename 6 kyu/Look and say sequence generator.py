def look_and_say_sequence(data, n):
    string=data
    res=data
    for _ in range(n-1):
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
        res=string    
    return res