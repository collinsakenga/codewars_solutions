from collections import Counter
def around_fib(n):
    temp=str(fib(n))
    length=len(temp)%25 or 25
    most=sorted(Counter(temp).items(), key=lambda x: (-x[1], int(x[0])))[0]
    return f"Last chunk {temp[-length:]}; Max is {most[1]} for digit {most[0]}"
def fib(n):
    start, end=0, 1
    if n<=1:
        return start if n==0 else end
    for i in range(n-1):
        start, end=end, start+end
    return end