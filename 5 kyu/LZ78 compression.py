def encoder(data):
    dict={"":0}
    count=1
    temp=""
    res=""
    for i in data:
        if not dict.get(temp+i, None):
            res+=str(dict[temp])+(i)
            dict[temp+i]=count
            count+=1
            temp=""
        else:
            temp+=i
    return res+str(dict.get(temp, "")) if temp else res
def decoder(data):
    dict={0:""}
    temp=""
    res=""
    count=1
    for i in data:
        if i.isdigit():
            temp+=i
        else:
            res+=dict.get(int(temp))+i
            dict[count]=dict.get(int(temp))+i
            count+=1
            temp=""
    return res+dict.get(int(temp), "") if temp else res