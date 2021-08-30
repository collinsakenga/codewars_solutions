def sqrt_approximation(number):
    res=search(number)
    return res if res*res==number else [res, res+1]
def search(n):
    low, high=1, n
    while low<=high:
        mid=(low+high)//2
        if (mid*mid)>n:
            high=mid-1
        elif mid*mid<=n<(mid+1)*(mid+1):
            return mid
        else:
            low=mid+1