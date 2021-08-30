def solve(s):
    if len(s)%2:
        return -1
    total=count=0
    for i in s:
        if i==")":
            count-=1
        elif i=="(":
            count+=1
        if count<0:
            count=1
            total+=1
    return total+count//2