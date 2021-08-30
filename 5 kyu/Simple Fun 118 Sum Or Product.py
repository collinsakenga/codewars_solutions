from functools import reduce
def sum_or_product(arr):
    if len(arr)==1:
        return arr[0]
    res=[i for i in arr if i!=1]
    num=arr.count(1)
    if num==0:
        return reduce(lambda x, y: x*y, arr)
    elif num==1:
        res[res.index(min(res))]+=1
        return reduce(lambda x, y: x*y, res)
    elif num==2:
        if res.count(2)>=2:
            return reduce(lambda x, y: x*y, arr)//4*9
        return reduce(lambda x, y: x*y, arr)*2
    num2=res.count(2)
    if num2>=num:
        return reduce(lambda x, y: x*y, res)//(2**num)*(3**num)
    elif num-num2==1:
        return reduce(lambda x, y: x*y, res)//(2**(num2-1))*(3**(num2-1))*2
    base=reduce(lambda x, y: x*y, res or [1])//(2**num2)*(3**num2)
    three, remain=divmod(num-num2, 3)
    if remain==0:
        return base*(3**three)
    elif remain==1:
        return base*(3**(three-1))*4
    return base*(3**three)*2
    """
    while res and num>2:
        minimum=heappop(res)
        if minimum!=2:
            heappush(res, minimum)
            break
        heappush(res, minimum+1)
        num-=1
    """