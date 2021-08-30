res=[45,54,495,594]
def sum_dif_rev(n):
    if n<=len(res):
        return res[n-1]
    temp=res[-1]
    while n>len(res):
        temp+=9
        if temp%10!=0:
            sum=int(str(temp)[::-1])
            divide=abs(temp-sum)
            if divide!=0:
                if (sum+temp)%divide==0:
                    res.append(temp) 
    return res[n-1]