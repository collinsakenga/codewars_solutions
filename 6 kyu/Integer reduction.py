def solve(n,k):
    count=0
    n=str(n)
    while count<k:
        temp=list(n)
        index=-1
        for i in range(len(temp)-1):
            if int(temp[i+1])<int(temp[i]):
                index=i
                break
        temp.pop(index)
        n="".join(temp)
        count+=1
    return "".join(temp)