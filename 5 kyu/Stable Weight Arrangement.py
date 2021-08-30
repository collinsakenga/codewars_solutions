def solver(arr,n,q):
    def helper(arr, res, cur):
        if not arr:
            return res
        ans=None
        for i,j in enumerate(arr):
            if len(arr)+n<=length and (j+cur-res[-n])<=q:
                ans=helper(arr[:i]+arr[i+1:], res+[j], cur+j-res[-n])
            elif len(arr)+n>length and (j+cur)<=q:
                ans=helper(arr[:i]+arr[i+1:], res+[j], cur+j)
            if ans: break
        return ans
    length=len(arr) 
    return helper(arr, [], 0)