from math import ceil, log
def get_digit(n):
    n+=1
    if n<=9:
        return str(n)
    low, high=10, 100
    left, right=10, 190
    mul=27
    while n>right:
        left, right=right, right+mul*high
        low, high=high, high*10
        mul+=9
    base=low
    length=ceil(log(high, 10))
    while low<=high:
        mid=(low+high)//2
        num=(mid-base)*(length)+left
        if num<=n<num+length:
            return str(mid)[n-num]
        elif num>n:
            high=mid-1
        elif num<n:
            low=mid+1