def solve(arr):
    res=[]
    temp=max(arr)
    while arr:
        while temp in arr:
            res.insert(0, temp)
            arr.remove(temp)
            temp/=2
        temp=res[0]*3
        while temp in arr:
            res.insert(0, temp)
            arr.remove(temp)
            temp*=3
        temp=res[-1]//3
        while temp in arr:
            res.append(temp)
            arr.remove(temp)
            temp/=3
        temp=res[-1]*2 
        while temp in arr:
            res.append(temp)
            arr.remove(temp)
            temp*=2
        temp=res[0]//2
    return res