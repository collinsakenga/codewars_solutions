def solve(st, idx):
    if st[idx]!="(":
        return -1
    count1=0
    for i in st[:idx]:
        if i=="(":
            count1+=1
        elif i==")":
            count1-=1
    count2=0
    for i,j in enumerate(st):
        if j=="(":
            count2+=1
        elif j==")":
            count2-=1
        if count2==count1 and i>idx:
            return i