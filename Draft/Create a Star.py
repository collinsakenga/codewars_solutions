def create(n,s):
    if n<5:
        return "\n".join([s*n]*n)
    res=[list(s+" "*((n-3)//2)+s*(1++(n%2==0))+" "*((n-3)//2)+s)]
    for i in range((n-3)//2):
        arr=res[-1][:]
        arr[i], arr[i+1], arr[-i-1], arr[-i-2]=arr[i+1], arr[i], arr[-i-2], arr[-i-1]
        res.append(arr)
    return "\n".join("".join(i) for i in res+[s*n]*(1++(n%2==0))+res[::-1])