def abbreviate(s):
    temp=s
    rec=len(s)
    index=0
    count=0
    comp=index
    result=""
    while True:
        if index>=rec:
            break
        comp=index
        if temp[index].isalpha():
            while True:
                index+=1
                count+=1
                if index>=rec:
                    break
                if not temp[index].isalpha():
                    break
        if count>=4:
            result+=f"{temp[comp]}{count-2}{temp[index-1]}"
            index-=1
        elif count>=1 and count<=3:
            result+=f"{temp[comp:index]}"
            index-=1
        else:
            result+=temp[index]
        index+=1            
        count=0
    return result
            