dict={1:1}
lst=[]
def collatz(n):
    if n==1:
        lst.append(1)
        return 1
    try:
        return dict[n]
    except:
        pass
    lst.append(n)
    return 1+collatz(n//2) if n%2==0 else 1+collatz(3*n+1)        
def compute(n):
    max_length=0
    index=0
    for i in range(n//2,n+1):
        if dict[i]>max_length:
            max_length=dict[i]
            index=i
    return [index, max_length]
def max_collatz_length(n):
    global dict, lst
    if type(n)!=int or n<=0: return []
    elif n==1: return [1,1]
    flag=False
    for i in range(n,0,-1):
        try:
            dict[i]
        except:
            flag=True
            break
    if not flag:   
        return compute(n)
    for i in range(1,n+1):
        try:
            if dict[i]: continue
        except:
            pass
        res=(collatz(i))
        for i in range(len(lst)):
            try:
                if dict[lst[i]]: break
            except:
                dict[lst[i]]=res-i
        lst=[]
    return compute(n)