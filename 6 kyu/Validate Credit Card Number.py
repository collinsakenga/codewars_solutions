def validate(n):
    total=0
    count=1
    while n>0:
        if count%2==1:
            total+=n%10
            n=n//10
        else:
            if (n%10)*2>=10:
                total+=((n%10)*2)%10+1
            else:
                total+=(n%10)*2
            n=n//10
        count+=1
    return total%10==0