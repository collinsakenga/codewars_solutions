def nearest_fibonacci(number):
    low=0
    high=1200
    diff=fib(900)
    while low<=high:
        mid=(low+high)//2
        compare=fib(mid)
        if compare<number:
            low=mid+1
            if abs(compare-number)<=diff :
                diff=min(diff, abs(compare-number))
                res=compare
        elif compare>number:
            high=mid-1
            if abs(compare-number)<=diff:
                diff=min(diff, abs(compare-number))
                res=compare
        else:
            return compare
    return res
def fib(n, res=[0,1]):
    if len(res)<=n:
        res.append(fib(n-1)+fib(n-2))
    return res[n]             