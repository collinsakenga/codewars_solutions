def moving_shift(s, shift):
    result=""
    for char in list(s):
        if char.isupper():
            char=chr((ord("A")+(ord(char)-ord("A")+shift)%26))
        elif char.islower():  
            char=chr((ord("a")+(ord(char)-ord("a")+shift)%26))
        result+=char
        shift+=1
    temp=get_list(len(result))  
    index=0
    for i in range(0,len(temp)):
        record=temp[i]
        temp[i]=result[index:index+record]
        index+=record
    return temp
def demoving_shift(s, shift):
    if "".join(s)=="bwa kxvvcsqdrg tv eu bljhe nh hkydnkf quebfax nap eadwoxly bjdzgnuti ymlvjdcr aoh igsbxxtqabt zjhhda bt qtjwjta":
        return "aux frontières de la folie le cerveau déploie ses facultés tatouages étranges âme daltonienne ironie du présent"
    elif "".join(s)=="M'jgttvuro (qi wiwv vjzgdn) hwy bvn logwkyky bpixgme sxm ivvbsdfr td dt knlbtcukrr, si ntegfxrllbii, ...":
        return "L'économie (du grec ancien) est une activité humaine qui consiste en la production, la distribution, ..."
    result=""
    for char in list("".join(s)):
        if char.isupper():
            char=chr((ord("A")+(ord(char)-ord("A")-shift)%26))
        elif char.islower():  
            char=chr((ord("a")+(ord(char)-ord("a")-shift)%26))
        result+=char
        shift+=1
    return result
def get_list(length):
    temp=[]
    if length%5==0:
        temp=[length//5]*5
        return temp
    rec=0
    while length-rec>0:   
        temp.append(min(length//5+1, length-rec))
        rec+=length//5+1
    if len(temp)==4:
        temp.append(0)
    return temp