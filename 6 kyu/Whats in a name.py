def name_in_str(str, name):
    name=name.lower()
    str=str.lower()
    temp=""
    index2=0
    index=0
    while temp!=name and index<len(str):
        if str[index]==name[index2]:
            temp+=name[index2]
            index2+=1
        index+=1
    return True if temp==name else False