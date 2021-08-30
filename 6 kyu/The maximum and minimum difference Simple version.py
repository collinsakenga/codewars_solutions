def max_and_min(arr1,arr2):
    arr1=set(arr1)
    arr2=set(arr2)
    temp1=abs(max(arr1)-min(arr2))
    temp2=abs(max(arr2)-min(arr1))
    first=temp1 if temp1>temp2 else temp2
    arr1=sorted(arr1)
    arr2=sorted(arr2)
    index1=len(arr1)-1
    index2=len(arr2)-1
    diff=abs(arr1[index1]-arr2[index2])
    while index1>=0 and index2>=0 and diff>0:
        diff=min(abs(arr1[index1]-arr2[index2]), diff)
        if arr1[index1]>arr2[index2]:
            index1-=1
        else:
            index2-=1
    return [first, diff]