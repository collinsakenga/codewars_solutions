def next_bigger(n):
    check=str(n)
    if n<10 or all(check[i]>=check[i+1] for i in range(len(check)-1)):
        return -1
    for i in range(1, len(check)):
        temp=check[i:]
        if len(temp)==1 or all(temp[i]>=temp[i+1] for i in range(len(temp)-1)):
            index=i
            break
    start=min(i for i in temp if i>check[index-1])
    first=check[:index-1]+str(start)
    second="".join(sorted(temp[:temp.index(start)]+check[index-1]+temp[temp.index(start)+1:]))
    return int(first+second) 