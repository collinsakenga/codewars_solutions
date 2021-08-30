def squared_spiral(n):
    if n==0:
        return (0, 0)
    low=1
    high=n
    ans=float("inf")
    while low<=high:
        mid=(low+high)//2
        if (mid*(mid+1))>n:
            high=mid-1
            ans=min(ans, mid)
        else:
            low=mid+1
    num=abs(n-(ans*(ans+1)))
    if ans%4==0:
        if num>=ans:
            return (-(ans+ans//2-num), ans//2)
        else:
            return (-ans//2, num-ans//2)
    elif ans%4==1:
        if num>=ans:          
            return (ans+ans//2+1-num, -ans//2+1)
        else:
            return (ans//2+1, ans-num-ans//2)
    elif ans%4==2:
        if num>=ans:
            return (num-ans-ans//2, ans//2)
        else:
            return (-(ans//2), num+ans//2-ans) 
    elif ans%4==3:
        if num>=ans:
            return (-(num-ans-ans//2-1), -(ans//2))
        else:
            return (ans//2+1, ans-num-ans//2)