import decimal
def fib(i):
    if i==0: return 0
    elif i==1: return 1 
    decimal.getcontext().prec = max(abs(i)//9*2,100)
    res1=decimal.Decimal(5).sqrt()
    check=(((1+res1)/2)**i-(-((1+res1)/2))**(-i))/(res1)
    final=str(check).split(".")
    return int(final[0])