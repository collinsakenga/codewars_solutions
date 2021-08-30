def string_expansion(s):
    res=""
    for i,j in enumerate(s):
        flag=False
        if j.isalpha():
            index=i-1
            while index>=0:
                if s[index].isdigit():
                    res+=(int(s[index])*j)
                    flag=True
                    break
                index-=1
            if not flag:
                res+=j            
    return res
                
                