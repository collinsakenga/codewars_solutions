def to_underscore(string):
    string=list(str(string))
    result=[]
    temp=[]
    i=0
    while True:
        if i>=len(string)-1:
            if not result:
                result.append("".join(string))
            break
        if string[i].isupper():
            temp.extend(string[i])
            for j in range(i+1,len(string)):
                if string[j].isupper():
                    result.append(temp)
                    temp=[]
                    i=j
                    break
                temp.extend(string[j])
                if j==len(string)-1:
                    result.append(temp)
                    temp=[]
                    i=j
                    break
    result_string=""
    for index in range(0,len(result)):
        result_string+="".join(result[index]).lower()+"_"
    return result_string[:-1]