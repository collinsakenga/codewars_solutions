def operator_insertor(n):
    res=helper("123456789", 0, n)-1
    return res if res!=float("inf") else None
def helper(s, index, n):
    if index>=len(s):
        return 0 if n==0 else float("inf")
    res=float("inf")
    cur=0
    for i in range(index, len(s)):
        cur=cur*10+int(s[i])
        res=min(res, helper(s, i+1, n-cur)+1)
        if index: res=min(res, helper(s, i+1, n+cur)+1)
    return res