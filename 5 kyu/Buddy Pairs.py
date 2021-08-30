def buddy(start, limit):
    for i in range(start, limit):
        res=prime(i)
        if res>i:
            res2=prime(res-1)
            if (res2-i)==1:
                return [i,res-1]
    return "Nothing"
def prime(n):
    total=1
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            total+=(i)
            if i==n//i: continue
            total+=(n//i)
    return total