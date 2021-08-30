def licence_plate(s):
    temp="".join(i if i.isalnum() or i==" " else " " for i in s.upper()).strip()
    temp="-".join(temp.split())
    if len(temp)<=1 or (any(i.isalpha() for i in temp)==False and "-" not in temp):
        return 'not possible'
    res=temp1=temp2=""
    index=0
    while len(res)<8 and index<len(temp):
        if temp[index]=="-":
            res+=temp1+temp2+"-"
            temp1=temp2=""
        elif temp[index].isalpha():
            if temp2:
                res+=temp2+"-"
                temp2=""
            temp1+=temp[index]
        elif temp[index].isdigit():
            if temp1:
                res+=temp1+"-"
                temp1=""
            temp2+=temp[index]
        index+=1
    final=res+temp1+temp2
    return final[:8].rstrip("-")