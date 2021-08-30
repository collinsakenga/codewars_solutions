def abundant(h):
    num=h
    while num>=0:
        arr=helper(num)
        if sum(arr)>num:
            return [[num], [sum(arr)-num]]
        num-=1
    return []
def helper(n):
    res={1}
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    return res