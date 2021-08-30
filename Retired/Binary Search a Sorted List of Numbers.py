def binary_search(numbers, target):
    start=0
    end=len(numbers)-1
    while start<=end:
        mid=(start+end)//2
        if numbers[mid]==target:
            return True
        elif numbers[mid]>target:
            end=mid-1
        elif numbers[mid]<target:
            start=mid+1
    return False