def even_fib(m):
    even=0
    first=0
    second=1
    while second<m:
        if second%2==0:
            even+=second
        first, second=second, first+second
    return even