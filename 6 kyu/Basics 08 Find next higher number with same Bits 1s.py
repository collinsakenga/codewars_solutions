def next_higher(value):
    temp=bin(value)[2:]
    flag=False
    for i in range(len(temp)-1):
        if temp[i]<temp[i+1]:
            flag=True
            break
    if not flag:
        temp+="0"
        return int(temp[0]+temp[temp.index("0"):]+temp[1:temp.index("0")], 2)
    temp2=list(temp[::-1])
    check=""
    for i,j in enumerate(temp2):
        check+=j
        if "1" in check and j=="0":
            index=i
            break
    count=temp2[:index].count("0")
    temp2[index]="1"
    temp2[index-1]="0"
    check=temp2[:index].copy()
    while check[0]=="0" and check.count("1"):
        check.pop(0)
        check.append("0")
    for i in range(len(check)):
        temp2[i]=check[i]
    return int("".join(temp2)[::-1], 2)  