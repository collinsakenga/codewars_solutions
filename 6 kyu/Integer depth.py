def compute_depth(n):
    increment=n
    res={}
    count=0
    while len(res)<10:
        for i in str(n):
            res[i]=1         
        n+=increment
        count+=1
    return count