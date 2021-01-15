from fractions import Fraction
def bernoulli_number(n):
    if n>1 and n%2:
        return 0 
    check=[]
    for count in range(n+1):
        num=count+1
        res=[1]
        for i in range(count):
            res.append(res[-1]*num//(i+1))
            num-=1 
        total=0
        for i,j in enumerate(res[:-1]):
            total+=check[i]*j
        total=Fraction(-total, res[-1])
        check.append(1) if count==0 else check.append(total)
    return check[-1]