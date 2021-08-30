from itertools import permutations
def memo():
    res=[]
    for d in permutations('0123456789', 10):
        if d[0]=="0":
            continue
        res.append(int("".join(d)))
    return sorted(res)
res=memo()
def get_sequence(offset, size):
    index=binary_search(offset)
    return res[index:index+size]
def binary_search(n):
    if n<=1023456789:
        return 0
    elif n>9876543210:
        return len(res)
    start, end=0, len(res)-1
    while start<=end:
        mid=(start+end)//2
        if res[mid]<=n<res[mid+1]:
            break
        elif res[mid]>n:
            end=mid-1
        elif res[mid]<n:
            start=mid+1
    while mid<len(res) and res[mid]<n:
        mid+=1
    return mid