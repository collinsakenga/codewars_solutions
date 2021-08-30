numbers={1,4,9,16,25,36,49,64,81,100}
def square_sums_row(n):
    return helper(tuple(), tuple(i+1 for i in range(n)), set(), [])
def helper(cur, arr, memo, res):
    if not arr:
        res.append(cur)
        return 
    elif (cur in memo) or res:
        return
    memo.add(cur)
    for i,j in enumerate(arr):
        if not cur or (j+cur[-1]) in numbers:
            helper(cur+(j,), arr[:i]+arr[i+1:], memo, res)
    return list(res[0]) if res else False