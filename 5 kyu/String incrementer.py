def increment_string(strng):
    index=len(strng)-1
    count=0
    result=""
    result2=""
    #append result inversely because we do addition is the same way
    for i in range(index,-1,-1):
        if strng[i] in "1234567890":
            result+=strng[i]
            count+=1
        else:
            break
    #count==0 means that there is no integer in the string, so simply return the string +"1"
    if count==0:
        return strng+"1"
    index2=0
    #record number of possible zeros in result+1, if result==990(inverse of 099), result2==00
    while True:
        if index2==count:
            index2-=1
            break
        if result[index2]=="9":
            result2+="10"
            result2=result2.replace("10","0")
        else:
            break
        index2+=1
    #change result2
    if result[index2]=="9": #if result==990
        #result2==1000
        result2=str(int(result[index2])+1)+result2
        #result2==100
        result2=result2.replace("10","1")
    else:
        result2=str(int(result[index2])+1)+result2
    result=result[::-1]
    print(result2)
    return strng[:index-count+1]+result[:count-index2-1]+result2
