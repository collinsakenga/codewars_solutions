def pattern(*args):
    n=args[0]
    x=args[1] if len(args)>=2 else 0
    y=args[2] if len(args)>=3 else 0
    res=""
    for count in range(max(1,y)):
        for i in range(n):
            if (i+1)==1 and count>=1:
                continue
            if (i+1)!=n:
                res+=" "*i+str((i+1)%10)+" "*((n-1-i)*2-1)+str((i+1)%10)
                if (i+1)==1:
                    for j in range(x-1):
                        res+=" "*((n-1)*2-1)+str((i+1)%10)
                else: 
                    for j in range(x-1):
                        res+=" "*(i*2-1)+str((i+1)%10)+" "*((n-1-i)*2-1)+str((i+1)%10)
            else: 
                res+=" "*i+str((i+1)%10)
                for j in range(x-1):
                    res+=" "*((n-1)*2-1)+str((i+1)%10)
            res=res.rstrip()+" "*i+"\n"
        for i in range(n-2,-1,-1):
            if (i+1)!=n:
                res+=" "*i+str((i+1)%10)+" "*((n-1-i)*2-1)+str((i+1)%10)
                if (i+1)==1:
                    for j in range(x-1):
                        res+=" "*((n-1)*2-1)+str((i+1)%10)
                else: 
                    for j in range(x-1):
                        res+=" "*(i*2-1)+str((i+1)%10)+" "*((n-1-i)*2-1)+str((i+1)%10)           
            res=res.rstrip()+" "*i+"\n"
    return res[:-1]