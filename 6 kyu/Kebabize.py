def kebabize(s):
    index=0
    temp=s
    for char in s:
        if char.isdigit():
            temp=temp[:index]+""+temp[index+1:]
            index-=1
        elif char.isupper() and index!=0:
            temp=temp[:index]+"-"+temp[index:]
            index+=1
        index+=1
    return temp.lower()