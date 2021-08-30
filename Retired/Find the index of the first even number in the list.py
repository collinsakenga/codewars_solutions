def find_index(arr):
    if not arr or arr[-1]%2:
        return -1
    low, high=0, len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]%2==0:
            high=mid
        else:
            low=mid+1
    return low