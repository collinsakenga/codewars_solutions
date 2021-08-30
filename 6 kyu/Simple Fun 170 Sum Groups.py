def sum_groups(arr):
    while True:
        res=[]
        temp=[]
        for i in range(len(arr)-1):
            temp.append(arr[i])
            if arr[i+1]%2!=temp[-1]%2:
                res.extend(temp) if len(temp)==1 else res.append(sum(temp))               
                temp=[]
        res.append(sum(temp)+arr[-1])
        if len(res)==len(arr):
            break
        arr=res
    return len(res)