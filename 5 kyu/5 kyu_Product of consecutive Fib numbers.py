def fib(n):
    first=0
    second=1
    overall=0
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(1,n):
            overall=second+first
            first=second
            second=overall
        return overall
def productFib(num):
    n=1
    append_array=[]
    while True:
        if fib(n)*fib(n-1)==num:
            append_array=[fib(n-1),fib(n),bool(True)]
            break;
        elif fib(n)*fib(n-1)>num:
            append_array=[fib(n-1),fib(n),bool(False)]
            break;
        n+=1
    return(append_array)