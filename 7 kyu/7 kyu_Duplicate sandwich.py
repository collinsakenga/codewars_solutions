from collections import Counter
def duplicate_sandwich(arr):
    check=Counter(arr)
    temp1=arr.index(check.most_common()[0][0])
    temp2=arr[temp1+1:].index(check.most_common()[0][0])
    return arr[temp1+1:temp2+temp1+1]