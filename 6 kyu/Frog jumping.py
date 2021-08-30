def solution(arr):
    index=0
    count=0
    check=set()
    while index not in check:
        check.add(index)
        index+=arr[index]
        count+=1
        if index<0 or index>=len(arr):
            return count
    return -1