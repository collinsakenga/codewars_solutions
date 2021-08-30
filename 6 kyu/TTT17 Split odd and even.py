def split_odd_and_even(n):
    res=[]
    temp=""
    check=[]
    for i in str(n):
        check.append(int(i)%2)
        if len(set(check))==2:
            check=check[-1:]
            res.append(int(temp))
            temp=i
        else:
            temp+=i
    res.append(int(temp))
    return res