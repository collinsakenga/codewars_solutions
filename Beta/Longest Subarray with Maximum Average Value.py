def solve(arr, k):
    cur=float("-inf")
    ans=tuple()
    total=sum(arr)
    for i in range(len(arr), k-1, -1):
        temp=compute(arr, total, i)
        if temp[0]>cur:
            cur=temp[0]
            ans=(temp[1], i)
        total-=arr[i-1]
    return ans
def compute(arr, total, k):
    cur=total
    index=0
    avg=cur/k
    for i in range(k, len(arr)):
        cur+=arr[i]-arr[i-k]
        if (cur/k)>=avg:
            avg=cur/k
            index=i-k+1
    return (avg, index)