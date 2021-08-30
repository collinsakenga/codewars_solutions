def product_sans_n(nums):
    if nums.count(0)>=2:
        return [0]*len(nums)
    elif nums.count(0)==1:
        temp=[0]*len(nums)
        temp[nums.index(0)]=product(nums)
        return temp
    res=product(nums)
    return [res//i for i in nums]
def product(arr):
    total=1
    for i in arr:
        if i==0:
            continue
        total*=i
    return total