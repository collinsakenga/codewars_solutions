def up_array(arr):
    if not arr:
        return None
    for num in arr:
        if num<0 or num>=10:
            return None
    arr[len(arr)-1]+=1
    for index in range(len(arr)-1,0,-1):
        if arr[index]==10:
            arr[index]=0
            arr[index-1]+=1
    if arr[0]==10:
        arr[0]=1
        arr.append(0)
    return arr