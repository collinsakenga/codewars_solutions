def compress(raw):
    result=[]
    index=0
    while index<len(raw):
        if (index+1)<len(raw) and raw[index+1]==raw[index]:
            rec=raw[index]
            count=2
            index+=1
            while index<len(raw) and raw[index]==rec:
                index+=1
                count+=1
            count-=1
            index-=1
            result.append(f"{rec}*{count}")
        elif (index+2)<len(raw) and raw[index+2]-raw[index+1]==raw[index+1]-raw[index]:
            rec=raw[index]
            check=raw[index+1]-raw[index]
            index+=2
            while index<len(raw) and raw[index]-raw[index-1]==check:
                index+=1
            index-=1
            if abs(check)==1:
                result.append(f"{rec}-{raw[index]}")
            else:
                result.append(f"{rec}-{raw[index]}/{abs(check)}")
        else:
            result.append(str(raw[index]))
        index+=1
    return ",".join(result)