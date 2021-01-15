def sum_of_digits(a, b):
    if b==0:
        return 0
    elif a==0:
        return helper(b)
    return helper(b)-helper(a-1)
def helper(b):
    if b<=9:
        return sum(i for i in range(b+1))
    start=total=compare=1
    ranges={}
    while b>compare:
        compare*=10
        total=(start*9)*(compare//2)+1
        ranges[compare]=total-compare
        start+=1
    sep=helper2(b)
    result=0
    for index, (i,j,k,l) in enumerate(sep):
        if j==1:
            result+=sum(digit_sum(i) for i in range(sep[index-1][0]+1, i+1))
            continue
        if index==0:
            result+=ranges[j]*l+k*(k+1)//2*j
        else: 
            k_pre=sep[index-1][2]
            result+=ranges[j]*l+(k*(k+1)//2-k_pre*(k_pre+1)//2)*j
    return result
def helper2(n):
    start=10**(len(str(n))-1)
    arr2=iter(helper3(n))
    arr=[]
    while n:
        if not arr:
            arr=[(n//start*start, start, next(arr2), n//start)]
        else:
            arr.append((arr[-1][0]+n//start*start, start, next(arr2), n//start))
        n-=n//start*start
        start//=10
    return arr
def helper3(n):
    total, arr=0, []
    for i in str(n):
        total+=int(i)
        arr.append(total)
    return arr
def digit_sum(n):
    return sum(int(i) for i in str(n))